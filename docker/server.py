# server.py
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 9090

with HTTPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Server started on port {PORT}")
    httpd.serve_forever()
