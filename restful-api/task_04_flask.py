#!/usr/bin/python3
"""
task_04_flask:
    This module uses FLASK to handle both GET and POST requests.
    It creates a Flask server and handles routes to respond to different
    endpoints.
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

# Example dictionary: username(key) whole object(value)
# users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}}
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    usernames = list(users.keys())  # List of all the usernames
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def users_username(username):
    # Getting whole object(value) that corresponds with username(key)
    whole_obj = users.get(username)
    return jsonify(whole_obj)


@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json()  # Get incoming JSON data
    username = data.get('username')  # Parse through incoming JSON data
    users[username] = {
        "username": data.get("username"),
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
        }  # Add to users dictionary
    return jsonify({"message": "User added", "user": users[username]})  # Confirmation message


if __name__ == "__main__":
    app.run(debug=True)
