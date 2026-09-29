from venv import logger

from constants import Httpstatus
from helpers import JSONresponse
from webob import Request, Response

class Handlers:
    @staticmethod
    def generic_exception_handler(request: Request, excp: Exception) -> Response:
        logger.exception(excp)
        response = {
            "message": f"Unhandled Exception Occurred: {str(excp)}"
        }
        return JSONresponse(
            json_body=response,
            status=Httpstatus.INTERNAL_SERVER_ERROR
        )
        
    @staticmethod
    def url_not_found_handler(request: Request) -> Response:
        response = {
            "message": f"Requested path {request.path} does not exist. Please check the URL and try again"
        }
        return JSONresponse(
            json_body=response,
            status=Httpstatus.NOT_FOUND
        )
        
    @staticmethod
    def method_not_allowed_handler(request: Request) -> Response:
        response = {
            "message": f"Method {request.method} is not allowed for the requested URL {request.path}. Please check the allowed methods and try again."
        }
        return JSONresponse(
            json_body=response,
            status=Httpstatus.METHOD_NOT_ALLOWED
        )