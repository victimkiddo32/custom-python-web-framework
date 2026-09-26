import json
from webob import Request, Response
from constants import Httpstatus


def JSONresponse(
    json_body:dict|list=None,
    status: Httpstatus | int = Httpstatus.OK
) -> Response:
    
    # Serialize Python dictionary/list into JSON bytes
    body_bytes = json.dumps(json_body).encode("utf-8")
    
    # Return a WebOb Response object
    return Response(
        body=body_bytes,
        status=status.value if hasattr(status, 'value') else status,
        #If you pass an Enum member (e.g., Httpstatus.OK), hasattr(status, 'value') evaluates to True, extracting its numerical integer (200).
        #If you pass a plain integer (e.g., 200), it uses the integer directly.
        
        content_type="application/json",
        charset="utf-8"
    )
