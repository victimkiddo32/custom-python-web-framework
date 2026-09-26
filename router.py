from constants import Httpstatus, Inventory
from helpers import JSONresponse
from common_handlers import Handlers
from parse import parse
from webob import Request, Response

class RouteManager:
    def __init__(self):
        self.routes = {}
        
    # Standardize path to always have a leading slash: "/api/products"   
    def normalized_path(self, path: str) -> str:
        clean_path = path.strip().rstrip("/")
        return clean_path if clean_path else "/"
        
    def register_route(self, path: str, handler: callable) -> None:
        requested_path = self.normalized_path(path)
        if requested_path in self.routes:
            raise RuntimeError(f"Path '{requested_path}' is already bound to a handler.")
        self.routes[requested_path] = handler

    #Role: The pattern matcher and variable extractor.
    def _find_handler(self, requested_path: str) -> callable:
        requested_path = self.normalized_path(requested_path)
        
        if requested_path in self.routes:
            return self.routes[requested_path], {}
        
        #URL that contains path variables
        for path, handler in self.routes.items():
            parse_result = parse(path, requested_path)
            if parse_result is not None:
                return handler, parse_result.named
        return None, None
    #example:
    #path = "/api/products/{category}"
    #requested_path = "/api/products/mobile"
    #parse_result.named becomes {'category': 'mobile'}




    #dispatch method to handle incoming requests based on the path   
    def dispatch(self, http_request: Request) -> Response:
        # 1. Look up the matching controller function and dynamic path kwargs
        requested_path = self.normalized_path(http_request.path)
        handler, kwargs = self._find_handler(requested_path)
    
        #if a matching route was found, execute it with kwargs unpacked
        if handler is not None:
            return handler(http_request, **kwargs)
    
        return Handlers.url_not_found_handler(http_request)