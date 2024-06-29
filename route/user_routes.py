from flask import Blueprint
from controller.user_controller import create_user_controller, list_users_controller, get_user_controller, update_user_controller, delete_user_controller

user_bp = Blueprint('user', __name__)

user_bp.route('/', methods=['POST'])(create_user_controller)
user_bp.route('/', methods=['GET'])(list_users_controller)
user_bp.route('/<int:user_id>', methods=['GET'])(get_user_controller)
user_bp.route('/<int:user_id>', methods=['PUT'])(update_user_controller)
user_bp.route('/<int:user_id>', methods=['DELETE'])(delete_user_controller)
