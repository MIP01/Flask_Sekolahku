#Flask tidak mendukung success handler secara native
from flask import jsonify
# memberikan nilai default
def success_response(data, status_code=200, message="Success"):
    response = jsonify({
        'message': f"{status_code} {message}",
        'data': data
    })
    response.status_code = status_code
    return response

def success_handler(f):
    def decorator(*args, **kwargs):
        result = f(*args, **kwargs)
        if isinstance(result, tuple):
            data, status_code = result
            if status_code == 201:
                message = "Created"
            elif status_code == 202:
                message = "Accepted"
            else:
                message = "Success"
            return success_response(data, status_code, message)
        else:
            return success_response(result)
    decorator.__name__ = f.__name__
    return decorator
