from flask import request, jsonify, g
from module.admin_module import create_admin, get_all_admin, get_admin_by, update_admin, delete_admin
from middleware.validation import validate_input, UserSchema
from middleware.decorator_handler import role_required

@validate_input(UserSchema)
def create_admin_handler():
    data = request.get_json()
    admin, status_code = create_admin(data)
    
    if isinstance(admin, dict) and 'error' in admin:
        return jsonify(admin), status_code

    return jsonify(admin), status_code

@role_required(['administrator'])
def get_all_admin_handler():
    result, status_code = get_all_admin()

    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), status_code

@role_required(['administrator'])
def get_admin_by_handler(user_id):
    current_user = g.current_user

    admin, status_code = get_admin_by(user_id, current_user)
    
    if isinstance(admin, dict) and 'error' in admin:
        return jsonify(admin), status_code

    return jsonify(admin), status_code

@role_required(['administrator'])
@validate_input(UserSchema)
def update_admin_handler(user_id):
    current_user = g.current_user
    data = request.get_json()

    admin, status_code = update_admin(user_id, data, current_user)

    if isinstance(admin, dict) and 'error' in admin:
        return jsonify(admin), status_code
    
    return jsonify(admin), status_code

@role_required(['administrator'])
def delete_admin_handler(user_id):
    current_user = g.current_user
    admin, status_code = delete_admin(user_id, current_user)
    
    if isinstance(admin, dict) and 'error' in admin:
        return jsonify(admin), status_code

    return jsonify(admin), status_code