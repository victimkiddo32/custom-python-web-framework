import json

from constants import Httpstatus, Inventory
from helpers import JSONresponse
from middleware import ErrorHandlerMiddleware
from common_handlers import Handlers
from router import RouteManager

class Application:
    def __init__(self):
        self.routing_manager = RouteManager()
        
    def __call__(self,environ,start_response):
        return self.routing_manager.dispatch(environ, start_response)    
    
    def route(self,path:str):
        def decorator(handler:callable):
            self.routing_manager.register_route(path,handler)
            return handler
        return decorator

    
app=Application()
middleware = ErrorHandlerMiddleware(
    app=app,
    exception_handler=Handlers.generic_exception_handler
)

