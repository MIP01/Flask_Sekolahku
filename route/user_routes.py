from flask import Blueprint
from controller.user_controller import create_user_handler, get_all_user_handler, get_user_by_handler, update_user_handler, delete_user_handler

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/user', methods=['POST'])(create_user_handler)
user_bp.route('/user', methods=['GET'])(get_all_user_handler)
user_bp.route('/user/<int:user_id>', methods=['GET'])(get_user_by_handler)
user_bp.route('/user/<int:user_id>', methods=['PUT'])(update_user_handler)
user_bp.route('/user/<int:user_id>', methods=['DELETE'])(delete_user_handler)
