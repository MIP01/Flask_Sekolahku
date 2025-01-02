from model import db, Courses
from sqlalchemy.exc import IntegrityError

def create_courses(data):
    try:
        course = Courses(
            course=data['course'],
            mentor=data['mentor'],
            title=data['title']
        )

        db.session.add(course)
        db.session.commit()

        return {"success": "Berhasil membuat course", "data": course.to_dict()}, 201

    except IntegrityError:
        db.session.rollback()  # Rollback untuk membersihkan sesi
        return {"error": "Email sudah terdaftar. Silakan gunakan Email lain."}, 409

def get_all_courses():
    user_list = Courses.query.all()

    if not user_list:
        return {'error': 'Tidak ada data yang ditampilkan'}, 404

    # Gunakan to_dict() untuk setiap course
    result = [course.to_dict() for course in user_list]
    
    return result, 200

def get_courses_by(course_id):
    course = Courses.query.get(course_id)

    if not course:
        return {"error": "Courses tidak ditemukan."}, 404

    return course.to_dict(), 200

def update_courses(course_id, data):
    course = Courses.query.get(course_id)

    if not course:
        return {"error": "Courses tidak ditemukan."}, 404

    course.course = data['course']
    course.mentor = data['mentor']
    course.title = data['title']
    db.session.commit()

    return {"success": "Data course berhasil diperbaharui", "data": course.to_dict()}, 200

def delete_courses(course_id):
    course = Courses.query.get(course_id)

    if not course:
        return {"error": "Courses tidak ditemukan."}, 404

    db.session.delete(course)
    db.session.commit()
    return {"success": "Courses berhasil dihapus."}, 200
