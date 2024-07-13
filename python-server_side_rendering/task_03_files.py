#!/usr/bin/python3
"""Basic flask application that renders a HTML template"""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Read and and load items from json file to python dict
    with open('items.json') as f:
        data = json.load(f)
    # retrieve values of "items" key
    # assign empty list if 'items' not present
    items = data.get('items', [])

    # Put items into html template
    return render_template('items.html', items=items)

@app.route('/products')
def product():
    data = []
    source = request.args.get('source')
    id = request.args.get('id')

    if id is not None:
        try:
            id = int(id)
        except ValueError:
            return render_template('product_display.html', error="Invalid ID format")

    if source == "json":
        data = load_json_data("products.json", id)
    elif source == "csv":
        data = load_csv_data("products.csv", id)
    else:
        return render_template('product_display.html', error="Wrong source")

    if not data:
        return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', data=data, source=source, id=id)

def load_json_data(filename, wanted_id=None):
    """ Load JSON data from file and returns as dictionary """
    data = []
    try:
        with open(filename, 'r') as f:
            rows = json.load(f)
        for row in rows:
            if wanted_id is None or row['id'] == wanted_id:
                data.append(row)
    except ValueError:
        return []

    return data

def load_csv_data(filename, wanted_id=None):
    """ Load CSV data from file and returns as dictionary """
    data = []
    try:
        with open(filename, 'r') as csvfile:
            for row in csv.DictReader(csvfile):
                row['id'] = int(row['id'])  # Convert ID to integer
                if wanted_id is None or row['id'] == wanted_id:
                    data.append(row)
    except ValueError:
        return []

    return data

if __name__ == '__main__':
    app.run(debug=True, port=5000)
