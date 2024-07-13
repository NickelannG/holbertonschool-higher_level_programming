#!/usr/bin/python3
"""Basic flask application that renders an HTML template"""
from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

# Routes for different pages
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for displaying items from JSON
@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
        items = data.get('items', [])
    except FileNotFoundError:
        items = []
    
    return render_template('items.html', items=items)

# Route for displaying products with optional filtering by source (json/csv) and id
@app.route('/products')
def product():
    data = []
    source = request.args.get('source')
    wanted_id = request.args.get('id')

    if source == "json":
        data = load_json_data("products.json", wanted_id)
    elif source == "csv":
        data = load_csv_data("products.csv", wanted_id)
              
    return render_template('product_display.html', data=data, source=source, id=wanted_id)

# Function to load JSON data from file and filter by id if provided
def load_json_data(filename, wanted_id=None):
    data = []

    try:
        with open(filename, 'r') as f:
            products = json.load(f)
            
        for product in products:
            if (wanted_id is not None and product['id'] == wanted_id) or (wanted_id is None):
                data.append(product)

        if wanted_id and not any(product['id'] == wanted_id for product in products):
            raise ValueError("Product with id {} not found in JSON source".format(wanted_id))

    except FileNotFoundError:
        raise ValueError("File '{}' not found".format(filename))
    except ValueError as e:
        raise ValueError("Unable to load data from file '{}': {}".format(filename, str(e)))

    return data

# Function to load CSV data from file and filter by id if provided
def load_csv_data(filename, wanted_id=None):
    data = []

    try:
        with open(filename, 'r') as csvfile:
            for row in csv.DictReader(csvfile):
                if (wanted_id is not None and row['id'] == wanted_id) or (wanted_id is None):
                    data.append(row)
    except Exception as e:
        raise ValueError("Unable to load data from file '{}': {}".format(filename, str(e)))

    return data

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
