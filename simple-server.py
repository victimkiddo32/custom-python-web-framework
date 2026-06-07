from wsgiref.simple_server import make_server
import json
class Httpstatus:
    OK="200 OK"

class ContentType:
    TEXT=('Content-Type', 'text/plain')
    JSON = ('Content-Type', 'application/json')


def application(environ, start_response):
    # print("In my application")
    # response_body=[
    #     f"{key}:{value}" for key,value in sorted(environ.items())
    # ]
    # response_text="\n".join(response_body)
    # response_headers=[
    #     ContentType.TEXT
    # ]
    # start_response(Httpstatus.OK, response_headers)

    # return [response_text.encode("utf-8")]

    path=environ.get('PATH_INFO','/')
    response_body=f"Responding from my application PATH : {path}"
    data=[
        {
            "product_id":1,
            "product_name":"Samsung"
        },

        {
            "product_id":2,
            "product_name":"Apple"
        }
    ]
    
    response_body=json.dumps(data)

    # set response status and headers
    status=Httpstatus.OK
    response_headers=[
        ContentType.JSON
    ]

    start_response(status,response_headers)
    
    #return response body as bytes
    return [response_body.encode("utf-8")]




if __name__ == '__main__':
    host='localhost'
    port=8000
    server= make_server(host, port, application)
    print(f"Listening on http://{host}:{port}")
    server.serve_forever()


