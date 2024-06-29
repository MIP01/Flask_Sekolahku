from flask import jsonify
from werkzeug.exceptions import HTTPException, NotFound

class ResourceNotFoundError(Exception):
    pass

def error_handler(app):

    @app.errorhandler(NotFound)
    def handle_not_found(error):
        response = jsonify({
            'error': 'Not Found',
            'message': str(error)
        })
        response.status_code = 404
        return response

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        response = jsonify({
            'error': 'HTTP Exception',
            'message': str(error)
        })
        response.status_code = error.code
        return response

    @app.errorhandler(Exception)
    def handle_general_exception(error):
        response = jsonify({
            'error': 'Internal Server Error',
            'message': str(error)
        })
        response.status_code = 500
        return response
