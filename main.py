#this main file is for gunicorn server
#it will not be used when running the wsgi-server.py file

#Using gunicorn because it is a production ready server and can handle multiple requests at once, 
#unlike the wsgiref server which is single threaded and can only handle one request at a time.

from app import middleware as app

import product_controller 
# Importing product_controller registers all @app.route decorators!

