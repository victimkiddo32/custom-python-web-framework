class ErrorHandlerMiddleware:
    def __init__(self, app, exception_handler:callable):
        self.app = app
        self.exception_handler = exception_handler

    def __call__(self, environ, start_response):
        try:
            return self.app(environ,start_response)
        except Exception as e:
            return self.exception_handler(environ, start_response, e)
        
