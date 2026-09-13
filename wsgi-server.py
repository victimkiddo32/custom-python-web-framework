from wsgiref.simple_server import make_server
from app import middleware

# Importing product_controller registers all @app.route decorators!
import product_controller

if __name__ == '__main__':
    host = 'localhost'
    port = 8080
    
    server = make_server(host, port, middleware)
    print(f"Listening on http://{host}:{port}")
    server.serve_forever()