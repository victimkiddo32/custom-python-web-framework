from constants import Httpstatus, Inventory
from helpers import JSONresponse


class RouteManager:
    def __init__(self):
        self.routes={}
        
    def register_route(self,path:str,handler:callable)->None:
        # Standardize path to always have a leading slash: "/api/products"
        normalized_path = "/" + path.strip("/")
        if normalized_path in self.routes:
            raise RuntimeError(f"Path '{normalized_path}' is already bound to a handler.")
        self.routes[normalized_path] = handler
    
    
    #dispatch method to handle incoming requests based on the path   
    def dispatch(self,environ,start_response):
        raw_path = environ.get('PATH_INFO', '/')
        # Standardize incoming PATH_INFO to match the registry key
        normalized_path = "/" + raw_path.strip("/")
        
        
        # Check if route handler exists in registered routes
        handler = self.routes.get(normalized_path)
        if handler:
            return handler(environ, start_response)
        
        
        # Return 404 NOT FOUND when path is not registered
        error_payload = {"error": f"Path '{raw_path}' not found."}
        return JSONresponse(error_payload, start_response, status=Httpstatus.NOT_FOUND)