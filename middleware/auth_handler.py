from flask import request, jsonify, make_response
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from model import Administrator, User
from middleware.decorator_handler import role_required
from middleware.validation import LoginSchema, validate_input

@validate_input(LoginSchema)
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Inisialisasi variabel
    user = None
    role = None

    # Cek apakah user adalah Administrator
    user = Administrator.query.filter_by(email=email).first()
    if user:
        role = user.role
    else:
        # Jika bukan Administrator, cek apakah user adalah User
        user = User.query.filter_by(email=email).first()
        if user:
            role = user.role

    # Jika user ditemukan, periksa password
    if user and password:
        # Tentukan identity berdasarkan role
        if role == 'administrator':
            identity = {'id': user.administrator_id, 'role': 'administrator'}
        else:
            identity = {'id': user.user_id, 'role': 'user'}
        
        # Buat access token
        access_token = create_access_token(identity=identity)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@role_required()
def logout():
    response = jsonify({"message": "Logout successful"})
    unset_jwt_cookies(response)  # Hapus token JWT dari cookies
    return make_response(response), 200