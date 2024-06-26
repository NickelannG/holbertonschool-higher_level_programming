#!/usr/bin/python3
"""
task_03_http_server:
    This module creates a simple HTTP server.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


HOST = "localhost"
PORT = 8000


class RequestHandler(BaseHTTPRequestHandler):
    """
    This class handles the HTTP requests
    """
    def do_GET(self):
        """
        GET requests
        """
        if self.path == '/':
            response = "Hello, this is a simple API!"

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(response.encode())

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json_data, "utf-8"))

        elif self.path == '/status':
            response = "OK"

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(response.encode())

        elif self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            json_info = json.dumps(info)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json_info, "utf-8"))

        else:
            response = "Endpoint not found"

            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(response.encode())

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), RequestHandler)
    print(f"Server running on {HOST}:{PORT}")
    server.serve_forever()
