from flask import request, jsonify
from module.user_module import create_user, get_users, get_user, update_user, delete_user
from middleware.success_handler import success_handler

@success_handler
def create_user_controller():
    data = request.get_json()
    new_user= create_user(data)
    return new_user, 201

@success_handler
def list_users_controller():
    users = get_users()
    return users

@success_handler
def get_user_controller(user_id):
    user = get_user(user_id)
    return user

@success_handler
def update_user_controller(user_id):
    data = request.json
    updated_user = update_user(user_id, data)
    return updated_user, 201

@success_handler        
def delete_user_controller(user_id):
    success = delete_user(user_id)
    return success