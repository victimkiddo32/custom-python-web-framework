import json

from constants import Httpstatus


def JSONresponse(response: dict | list[dict], 
                 start_response, 
                 status: Httpstatus
                 )-> list[bytes]:
                 
    response_body = json.dumps(response).encode("utf-8")
    response_headers = [("Content-Type", "application/json")]
    
    
    start_response(status, response_headers)
    return [response_body]
