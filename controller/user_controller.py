from flask import request, jsonify, g
from module.user_module import create_user, get_all_user, get_user_by, update_user, delete_user
from middleware.validation import validate_input, UserSchema
from middleware.decorator_handler import role_required

@validate_input(UserSchema)
def create_user_handler():
    data = request.get_json()
    user, status_code = create_user(data)
    
    if isinstance(user, dict) and 'error' in user:
        return jsonify(user), status_code

    return jsonify(user), status_code

@role_required(['user'])
def get_all_user_handler():
    result, status_code = get_all_user()

    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), status_code

@role_required(['user'])
def get_user_by_handler(user_id):
    current_user = g.current_user

    user, status_code = get_user_by(user_id, current_user)
    
    if isinstance(user, dict) and 'error' in user:
        return jsonify(user), status_code

    return jsonify(user), status_code

@role_required(['user'])
@validate_input(UserSchema)
def update_user_handler(user_id):
    current_user = g.current_user
    data = request.get_json()

    user, status_code = update_user(user_id, data, current_user)

    if isinstance(user, dict) and 'error' in user:
        return jsonify(user), status_code
    
    return jsonify(user), status_code

@role_required(['user'])
def delete_user_handler(user_id):
    current_user = g.current_user
    user, status_code = delete_user(user_id, current_user)
    
    if isinstance(user, dict) and 'error' in user:
        return jsonify(user), status_code

    return jsonify(user), status_code