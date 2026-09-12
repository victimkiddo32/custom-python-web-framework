from wsgiref.simple_server import make_server
import json

class Httpstatus:
    OK = "200 OK"
    NOT_FOUND = "404 NOT FOUND"

class ContentType:
    JSON = ('Content-Type', 'application/json')

Inventory = {
    "mobile": [
        {"product id": 1, "product name": "S25 ultra", "brand": "Samsung"},
        {"product id": 2, "product name": "Iphone", "brand": "Apple"}
    ],
    "laptop": [
        {"product id": 1, "product name": "Asus ROG", "brand": "Asus"},
        {"product id": 2, "product name": "Dell XPS", "brand": "Dell"}
    ]
}

def raw_application(environ, start_response):
    path = environ.get('PATH_INFO', '/')
    cleaned_path = path.strip('/')
    
    category = cleaned_path.split('/')[-1] if cleaned_path else ""
    
    if category in Inventory:
        status = Httpstatus.OK
        data = Inventory[category]
    elif category == "":
        status = Httpstatus.OK
        data = {"message": "Welcome Home! Try visiting /mobile or /laptop"}
    else:
        status = Httpstatus.NOT_FOUND
        data = {"error": f"Category '{category}' does not exist."}

    # Returns the status and data tuple to the middleware wrapper
    return status, data


class JSONMiddleware:
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        # Receives the tuple directly from raw_application
        status, data = self.app(environ, start_response)
        
        # Encodes the JSON payload into bytes once
        response_body = json.dumps(data).encode("utf-8")
        response_headers = [ContentType.JSON]
        
        start_response(status, response_headers)
        
        # Returns the bytes object cleanly in a list
        return [response_body]


if __name__ == '__main__':
    host = 'localhost'
    port = 8080
    
    Wrapped_app = JSONMiddleware(raw_application)
    server = make_server(host, port, Wrapped_app)
    print(f"Listening on http://{host}:{port}")
    server.serve_forever()