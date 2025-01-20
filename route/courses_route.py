from flask import Blueprint
from controller.courses_controller import create_courses_handler, get_all_courses_handler, get_courses_by_handler, update_courses_handler, delete_courses_handler
from controller.user_course_controller import create_user_course_handler, get_all_user_course_handler, get_course_participants_handler, get_commission_handler, update_user_course_handler, delete_user_course_handler

courses_bp = Blueprint('courses_bp', __name__)
user_course_bp = Blueprint('user_course', __name__)

courses_bp.route('/courses', methods=['POST'])(create_courses_handler)
courses_bp.route('/courses', methods=['GET'])(get_all_courses_handler)
courses_bp.route('/courses/<int:course_id>', methods=['GET'])(get_courses_by_handler)
courses_bp.route('/courses/<int:course_id>', methods=['PUT'])(update_courses_handler)
courses_bp.route('/courses/<int:course_id>', methods=['DELETE'])(delete_courses_handler)

user_course_bp.route('/pilihan', methods=['POST'])(create_user_course_handler)
user_course_bp.route('/pilihan', methods=['GET'])(get_all_user_course_handler)
user_course_bp.route('/pilihan/participant', methods=['GET'])(get_course_participants_handler)
user_course_bp.route('/pilihan/commission', methods=['GET'])(get_commission_handler)
user_course_bp.route('/pilihan/<int:userCourse_id>', methods=['PUT'])(update_user_course_handler)
user_course_bp.route('/pilihan/<int:userCourse_id>', methods=['DELETE'])(delete_user_course_handler)