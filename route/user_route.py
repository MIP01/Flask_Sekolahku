from flask import Blueprint
from controller.user_controller import create_user_handler, get_all_user_handler, get_user_by_handler, update_user_handler, delete_user_handler
from controller.admin_controller import create_admin_handler, get_all_admin_handler, get_admin_by_handler, update_admin_handler, delete_admin_handler

user_bp = Blueprint('user_bp', __name__)
admin_bp = Blueprint('admin_bp', __name__)

user_bp.route('/user', methods=['POST'])(create_user_handler)
user_bp.route('/user', methods=['GET'])(get_all_user_handler)
user_bp.route('/user/<int:user_id>', methods=['GET'])(get_user_by_handler)
user_bp.route('/user/<int:user_id>', methods=['PUT'])(update_user_handler)
user_bp.route('/user/<int:user_id>', methods=['DELETE'])(delete_user_handler)


admin_bp.route('/admin', methods=['POST'])(create_admin_handler)
admin_bp.route('/admin', methods=['GET'])(get_all_admin_handler)
admin_bp.route('/admin/<int:user_id>', methods=['GET'])(get_admin_by_handler)
admin_bp.route('/admin/<int:user_id>', methods=['PUT'])(update_admin_handler)
admin_bp.route('/admin/<int:user_id>', methods=['DELETE'])(delete_admin_handler)