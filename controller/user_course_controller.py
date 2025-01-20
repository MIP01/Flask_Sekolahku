from flask import request, jsonify, g
from module.user_course_module import create_user_course, get_all_user_course, get_course_participants, get_commission, update_user_course, delete_user_course
from middleware.validation import validate_input, UserSchema
from middleware.decorator_handler import role_required

@role_required(['user'])
def create_user_course_handler():
    data = request.get_json()

    current_user = g.current_user

    user, status_code = create_user_course(data, current_user)
    
    if isinstance(user, dict) and 'error' in user:
        return jsonify(user), status_code

    return jsonify(user), status_code

@role_required(['user','administrator'])
def get_all_user_course_handler():
    current_user = g.current_user

    result, status_code = get_all_user_course(current_user)

    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), status_code

@role_required(['administrator'])
def get_course_participants_handler():
    result, status_code = get_course_participants()

    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), status_code

@role_required(['administrator'])
def get_commission_handler():
    result, status_code = get_commission()

    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), status_code

@role_required(['user', 'administrator'])
def update_user_course_handler(userCourse_id):
    current_user = g.current_user
    data = request.get_json()

    user, status_code = update_user_course(userCourse_id, data, current_user)

    if isinstance(user, dict) and 'error' in user:
        return jsonify(user), status_code
    
    return jsonify(user), status_code

@role_required(['user','administrator'])
def delete_user_course_handler(userCourse_id):
    current_user = g.current_user
    user, status_code = delete_user_course(userCourse_id, current_user)
    
    if isinstance(user, dict) and 'error' in user:
        return jsonify(user), status_code

    return jsonify(user), status_code