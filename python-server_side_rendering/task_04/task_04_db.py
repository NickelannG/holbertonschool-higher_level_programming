#!/usr/bin/python3
"""Basic flask application that renders a HTML template"""
from flask import Flask, render_template, request
import json, csv, sqlite3

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


def load_sql_data(filename, wanted_id = None):
    """ Load SQLite data and return as dictionary """
    
    # Initialize an empty list to hold the data that will be fetched from the SQLite database
    data = []
    
    # Create the WHERE clause of the SQL query if a specific ID is requested
    where_clause = ""
    if wanted_id is not None:
        where_clause = " WHERE id = " + wanted_id
    
    # Connect to the SQLite database file
    con = sqlite3.connect(filename)
    cur = con.cursor()
    
    # Execute the SQL query to select all columns from the 'products' table, with an optional WHERE clause
    res = cur.execute("SELECT * FROM products " + where_clause)
    rows = res.fetchall()  # Fetch all the rows from the executed query
    
    # Get the column names from the cursor description
    keys = []
    colnames = cur.description
    for desc in colnames:
       # print(desc)
       keys.append(desc[0])
    
    # Alternatively, the column names could be manually set like this:
    # keys = ["id", "name", "category", "price"]
    
    # Convert each row from the database into a dictionary
    for row_tuple in rows:
        item = {}
        i = 0
        for v in row_tuple:
            item[keys[i]] = v
            i = i + 1
        data.append(item)  # Append each dictionary to the data list
    
    # Return the list of dictionaries containing the data
    return data

def create_database():
       """Create and populate the database"""
       conn = sqlite3.connect('products.db')
       cursor = conn.cursor()
       cursor.execute('''
           CREATE TABLE IF NOT EXISTS Products (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               category TEXT NOT NULL,
               price REAL NOT NULL
           )
       ''')
       cursor.execute('''
           INSERT INTO Products (id, name, category, price)
           VALUES
           (1, 'Laptop', 'Electronics', 799.99),
           (2, 'Coffee Mug', 'Home Goods', 15.99)
       ''')
       conn.commit()
       conn.close()

@app.route('/products')
def product():
    data = []
    source = request.args.get('source')
    id = request.args.get('id')
    

    if source == "json":
        data = load_json_data("products.json", id)
    elif source == "csv":
        data = load_csv_data("products.csv", id)
    elif source == "sql":
        create_database()
        data = load_sql_data("products.db", id)
              
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