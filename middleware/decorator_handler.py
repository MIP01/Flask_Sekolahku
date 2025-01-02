from flask import g, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps

def role_required(role=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Verifikasi token JWT
            verify_jwt_in_request()

            # Mendapatkan user_id dari JWT
            current_user = get_jwt_identity()
            if not current_user:
                return jsonify({"error": "Unauthenticated"}), 401
            
            # Menyimpan user yang sedang diautentikasi ke dalam `g`
            g.current_user = current_user
            
            # Pengecekan role jika diperlukan
            if role and current_user['role'] not in role:
                return jsonify({"error": "Unauthorized access"}), 403
            
            return func(*args, **kwargs)
        return wrapper
    return decorator