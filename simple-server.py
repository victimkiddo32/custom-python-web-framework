from wsgiref.simple_server import make_server
import json

class Httpstatus:
    OK = "200 OK"

class ContentType:
    JSON = ('Content-Type', 'application/json')

Inventory= {
    "mobile":[
        {
            "product id": 1,
            "product name": "S25 ultra",
            "brand": "Samsung"
        },
        {
            "product id": 2,
            "product name": "Iphone",
            "brand": "Apple"
        }
    ],
    "laptop":[
       {
            "product id": 1,
            "product name": "Asus ROG",
            "brand": "Asus"
        },
        {
            "product id": 2,
            "product name": "Dell XPS",
            "brand": "Dell"
        }
    ]
}

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

    path = environ.get('PATH_INFO', '/')
    cleaned_path = path.strip('/')
    
    # 2. Extract category, handling the root "/" homepage gracefully
    category = cleaned_path.split('/')[-1] if cleaned_path else ""
    

    # 3. Routing Logic
    if category in Inventory:
        status = Httpstatus.OK
        data = Inventory[category]
    elif category == "":
        status = Httpstatus.OK
        data = {"message": "Welcome Home! Try visiting /Mobile or /Laptop"}
    else:
        status = "404 NOT FOUND"
        data = {"error": f"Category '{category}' does not exist."}


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
    host = 'localhost'
    port = 8080
    server = make_server(host, port, application)
    print(f"Listening on http://{host}:{port}")
    server.serve_forever()

