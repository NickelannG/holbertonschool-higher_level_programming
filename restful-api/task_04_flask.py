#!/usr/bin/python3
"""
task_04_flask:
    This module uses FLASK to handle both GET and POST requests.
    It creates a Flask server and handles routes to respond to different
    endpoints.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    # List of all the usernames
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route("/status")
def status():
    # Return OK status
    return "OK"

@app.route("/users/<username>")
def users_username(username):
    # Getting whole object(value) that corresponds with username(key)
    whole_obj = users.get(username)
    if whole_obj:
        return jsonify(whole_obj)
    else:
        # Return error message if user not found
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=['POST'])
def add_user():
    # Get incoming JSON data
    data = request.get_json()
    # Parse through incoming JSON data
    username = data.get('username')
    if username is None:
        # Return error message if username is missing
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        # Return error message if username already exists
        return jsonify({"error": "Username already exists"}), 400

    # Add new user to the users dictionary
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    # Return confirmation message
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)
