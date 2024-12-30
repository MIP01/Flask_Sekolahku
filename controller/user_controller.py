from flask import request, jsonify
from module.user_module import create_user, get_all_user, get_user_by, update_user, delete_user
from middleware.validation import validate_input, UserSchema

@validate_input(UserSchema)
def create_user_handler():
    data = request.get_json()
    user, status_code = create_user(data)
    
    if isinstance(user, dict) and 'error' in user:
        return jsonify(user), status_code

    return jsonify(user), status_code

def get_all_user_handler():
    result, status_code = get_all_user()

    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), status_code

def get_user_by_handler(user_id):
    user, status_code = get_user_by(user_id)
    
    # Tangani error jika ada
    if isinstance(user, dict) and 'error' in user:
        return jsonify(user), status_code

    return jsonify(user), status_code

@validate_input(UserSchema)
def update_user_handler(user_id):
    data = request.get_json()
    user, status_code = update_user(user_id, data)

    # Jika mahasiswa tidak ditemukan, kembalikan error 404
    if isinstance(user, dict) and 'error' in user:
        return jsonify(user), status_code
    
    return jsonify(user), status_code

def delete_user_handler(user_id):
    user, status_code = delete_user(user_id)
    
    if isinstance(user, dict) and 'error' in user:
        return jsonify(user), status_code

    return jsonify(user), status_code