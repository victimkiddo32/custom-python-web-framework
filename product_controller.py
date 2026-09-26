from webob import Request, Response
from helpers import JSONresponse
from constants import Httpstatus, Inventory
from app import app

@app.route("/api/products")
def get_products(request: Request) -> Response:
    return JSONresponse(
        json_body=Inventory,
        status=Httpstatus.OK
    )    

@app.route("/")
def home(request: Request) -> Response:
    return JSONresponse(
        json_body={"message": "Welcome Home! Try visiting /api/products"},
        status=Httpstatus.OK
    )
    
@app.route("/api/products/{category}")
def get_products_by_category(request:Request, category: str) -> Response:
    if category not in Inventory:
        return JSONresponse(
            json_body={"error": f"Category '{category}' not found in inventory."},
            status=Httpstatus.NOT_FOUND
        )
        
    return JSONresponse(
        json_body=Inventory[category],
        status=Httpstatus.OK
    )
    