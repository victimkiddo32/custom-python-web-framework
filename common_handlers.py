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