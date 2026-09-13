from helpers import JSONresponse
from constants import Httpstatus, products
from app import app

@app.route("/api/products")
def get_products(environ, start_response):
    return JSONresponse(
        products,
        start_response,
        status=Httpstatus.OK
    )
    

@app.route("/")
def home(environ, start_response):
    return JSONresponse(
        {"message": "Welcome Home! Try visiting /api/products"},
        start_response,
        status=Httpstatus.OK
    )