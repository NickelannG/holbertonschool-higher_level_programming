#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'My_dog_Griff_is_cute'
jwt = JWTManager(app)

users = {
    "Nicole": {
        "username": "Nicole",
        "password": generate_password_hash("dog"),
        "role": "admin"
    },
    "Griffin": {
        "username": "Griffin",
        "password": generate_password_hash("treat"),
        "role": "moderator"
    }
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user in users and check_password_hash(user['password'], password):
        return user
    return None

@app.route("/")
@auth.login_required
def home():
    return "Hello, {}!".format(auth.current_user()['username'])


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"msg": "Bad username or password"}), 401

    # Generate JWT 
    access_token = create_access_token(
        identity={"username": username, "role": user['role']})
    return jsonify(access_token=access_token)


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=["GET"])
def admins_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"msg": "Admins only!"}), 403
    return "Admin Access: Granted".format(current_user['username'])


@app.route('/moderator-only', methods=["GET"])
def moderators_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'moderator':
        return jsonify({"msg": "Moderators only!"}), 403
    return "Moderator Access: Granted".format(current_user['username'])


# Error handlers for JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run(debug=True)