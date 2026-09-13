import json

class Httpstatus:
    OK = "200 OK"
    NOT_FOUND = "404 NOT FOUND"
    INTERNAL_SERVER_ERROR = "500 Internal Server Error"
    

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
