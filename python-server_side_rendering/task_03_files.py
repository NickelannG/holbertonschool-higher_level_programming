#!/usr/bin/python3
"""Basic flask application that renders a HTML template"""
from flask import Flask, render_template, request
import json, csv

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

    if source == "json":
        data = load_json_data("products.json", id)
    elif source == "csv":
        data = load_csv_data("products.csv", id)
              
    return render_template('product_display.html', data=data, source=source, id=id)

def load_json_data(filename, wanted_id = None):
    """ Load JSON data from file and returns as dictionary """

    data = []

    try:
        with open(filename, 'r') as f:
            rows = json.load(f)
        for row in rows:
            key = row['id']

            if (wanted_id is not None and key == wanted_id) or (wanted_id is None):
                # Create dict anyway
                product = {}
                # write to dict
                for key, values in row.items():
                    product[key] = values
                data.append(product)

    except: ValueError("Unable to load data from file '{}'".format(filename))

    return data

def load_csv_data(filename, wanted_id = None):
    """ Load CSV data from file and returns as dictionary """

    data = []

    try:
        with open(filename, 'r') as csvfile:
            # using DictReader method to convert each row to a dictionary
            for row in csv.DictReader(csvfile):
                if (wanted_id is not None and row['id'] == wanted_id) or (wanted_id is None):
                    data.append(row)
    except: ValueError("Unable to load data from file '{}'".format(filename))

    return data


if __name__ == '__main__':
    app.run(debug=True, port=5000)