from flask import request, jsonify, g
from module.courses_module import create_courses, get_all_courses, get_courses_by, update_courses, delete_courses
from middleware.validation import validate_input, UserSchema
from middleware.decorator_handler import role_required

@role_required(['administrator'])
def create_courses_handler():
    data = request.get_json()
    course, status_code = create_courses(data)
    
    if isinstance(course, dict) and 'error' in course:
        return jsonify(course), status_code

    return jsonify(course), status_code

@role_required(['user','administrator'])
def get_all_courses_handler():
    result, status_code = get_all_courses()

    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), status_code

    return jsonify(result), status_code

@role_required(['user','administrator'])
def get_courses_by_handler(course_id):

    course, status_code = get_courses_by(course_id)
    
    if isinstance(course, dict) and 'error' in course:
        return jsonify(course), status_code

    return jsonify(course), status_code

@role_required(['administrator'])
def update_courses_handler(course_id):
    data = request.get_json()

    course, status_code = update_courses(course_id, data)

    if isinstance(course, dict) and 'error' in course:
        return jsonify(course), status_code
    
    return jsonify(course), status_code

@role_required(['administrator'])
def delete_courses_handler(course_id):
    course, status_code = delete_courses(course_id)
    
    if isinstance(course, dict) and 'error' in course:
        return jsonify(course), status_code

    return jsonify(course), status_code