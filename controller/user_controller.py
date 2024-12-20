from flask import request, jsonify
from module.user_module import create_user, get_users, get_user_by, update_user, delete_user

def create_user_handler():
    data = request.get_json()
    result, status_code = create_user(data)
    
    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), 200

def get_users_handler():
    result = get_users()
    return jsonify(result), 200

def get_user_by_handler(user_id):
    result = get_user_by(user_id)
    
    # Tangani error jika ada
    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), 400

    return jsonify(result), 200

def update_user_handler(user_id):
    data = request.get_json()
    result, status_code = update_user(user_id, data)

    # Jika mahasiswa tidak ditemukan, kembalikan error 404
    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code
    
    return jsonify(result), status_code

    # Kembalikan data mahasiswa yang diperbarui
    return jsonify(result.to_dict()), 200

def delete_user_handler(user_id):
    result, status_code = delete_user(user_id)
    
    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), status_code