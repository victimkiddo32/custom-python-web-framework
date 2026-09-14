from constants import Httpstatus
from helpers import JSONresponse

class Handlers:
    @staticmethod
    def generic_exception_handler(environ, start_response, excp: Exception) -> list[bytes]:
        response = {
            "message": f"Unhandled Exception Occurred: {str(excp)}"
        }
        # Use a proper WSGI status string ("500 Internal Server Error")
        return JSONresponse(
            response=response,
            start_response=start_response,
            status=Httpstatus.INTERNAL_SERVER_ERROR
        )
        
    @staticmethod
    def url_not_found_handler(environ, start_response) -> list[bytes]:
        path=environ.get('PATH_INFO', '/')
        response={
            "message": f"Requested path {path} does not exist.Please check the URL and try again"
        }
        return JSONresponse(
            response,
            start_response,
            status=Httpstatus.NOT_FOUND
        )