import json

from constants import Httpstatus, Inventory
from helpers import JSONresponse
from middleware import ErrorHandlerMiddleware
from common_handlers import Handlers

class Application:
    def __init__(self):
        pass
    def __call__(self,environ,start_response,*args,**kwargs):
        path = environ.get('PATH_INFO', '/')
        cleaned_path = path.strip('/')
        category = cleaned_path.split('/')[-1] if cleaned_path else ""
        
        # Root URL check
        if not category:
            return JSONresponse(
                {"message": "Welcome Home! Try visiting /mobile or /laptop"}, 
                start_response, 
                status=Httpstatus.OK
            )
            
        if category in Inventory:
            products = Inventory[category]
            return JSONresponse(products, start_response, status=Httpstatus.OK)
        
       # Missing category handling
        error_payload = {"error": f"Category '{category}' does not exist."}
        return JSONresponse(error_payload, start_response, status=Httpstatus.NOT_FOUND)
        
        
app=Application()
middleware = ErrorHandlerMiddleware(
    app=app,
    exception_handler=Handlers.generic_exception_handler
)

