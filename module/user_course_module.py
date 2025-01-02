from model import db, UserCourse, User, Courses
from sqlalchemy.exc import IntegrityError

def create_user_course(data, current_user):
    try:
        # Jika role adalah 'user', gunakan user_id dari current_user
        if current_user['role'] == 'user':
            user_id = current_user['id']
        # Jika role adalah 'administrator', ambil user_id dari data
        elif current_user['role'] == 'administrator':
            if 'user_id' not in data:
                return {"error": "Administrator harus menyertakan user_id."}, 400
            user_id = data['user_id']
        else:
            return {"error": "Role tidak valid."}, 403

        user_course = UserCourse(
            user_id=user_id,
            course_id=data['course_id']
        )

        db.session.add(user_course)
        db.session.commit()

        return {"success": "Berhasil membuat user_course", "data": user_course.to_dict()}, 201

    except IntegrityError:
        db.session.rollback()  # Rollback untuk membersihkan sesi
        return {"error": "Email sudah terdaftar. Silakan gunakan Email lain."}, 409

def get_all_user_course(current_user):
    # Query semua data dengan join untuk mendapatkan detail user dan course
    query = db.session.query(
        UserCourse.userCourse_id,
        User.username,
        Courses.course,
        Courses.mentor,
        Courses.title
    ).join(User, User.user_id == UserCourse.user_id) \
     .join(Courses, Courses.course_id == UserCourse.course_id)

    # Jika user adalah role 'user', filter data hanya untuk user tersebut
    if current_user['role'] == 'user':
        query = query.filter(UserCourse.user_id == current_user['id'])

    # Eksekusi query dan format hasilnya
    user_courses = query.all()

    if not user_courses:
        return {'error': 'Tidak ada data yang ditampilkan'}, 404

    # Format hasil
    result = [
        {
            'userCourse_id': uc.userCourse_id,
            'username': uc.username,
            'course': uc.course,
            'mentor': uc.mentor,
            'title': uc.title
        }
        for uc in user_courses
    ]

    return result, 200

def get_course_participants():
    # Query untuk menghitung jumlah peserta didik per mata kuliah
    query = db.session.query(
        Courses.course,
        Courses.mentor,
        Courses.title,
        db.func.count(UserCourse.user_id).label('jumlah_peserta')
    ).join(UserCourse, Courses.course_id == UserCourse.course_id) \
     .group_by(Courses.course, Courses.mentor, Courses.title)

    # Eksekusi query
    course_participants = query.all()

    if not course_participants:
        return {'error': 'Tidak ada data peserta didik untuk mata kuliah'}, 404

    # Format hasil
    result = [
        {
            'course': cp.course,
            'mentor': cp.mentor,
            'title': cp.title,
            'jumlah_peserta': cp.jumlah_peserta
        }
        for cp in course_participants
    ]

    return result, 200

def update_user_course(userCourse_id, data, current_user):
    user_course = UserCourse.query.get(userCourse_id)

    if not user_course:
        return {"error": "UserCourse tidak ditemukan."}, 404

    # Verifikasi bahwa user hanya bisa mengupdate data miliknya sendiri
    if current_user['role'] == 'user' and user_course.user_id != current_user['id']:
        return {"error": "Unauthorized access to update this user_course"}, 403

    # Validasi input
    if 'course_id' not in data:
        return {"error": "Field 'course_id' harus disertakan."}, 400

    try:
        # Jika role adalah user, hanya bisa update miliknya sendiri
        if current_user['role'] == 'user':
            user_course.user_id = current_user['id']
        else:  # Administrator bisa mengubah user_id
            user_course.user_id = data.get('user_id', user_course.user_id)

        user_course.course_id = data.get('course_id', user_course.course_id)
        db.session.commit()

        return {"success": "Data user_course berhasil diperbaharui", "data": user_course.to_dict()}, 200

    except IntegrityError:
        db.session.rollback()
        return {"error": "Data user_course menyebabkan konflik. Periksa kembali input Anda."}, 409

def delete_user_course(userCourse_id, current_user):
    user_course = UserCourse.query.get(userCourse_id)

    if not user_course:
        return {"error": "UserCourse tidak ditemukan."}, 404

     # Verifikasi bahwa user_course yang sedang login hanya bisa menghapus dirinya sendiri
    if current_user['role'] == 'user' and user_course.user_id != current_user['id']:
        return {'error': 'Unauthorized access to delete this user_course'}, 403

    db.session.delete(user_course)
    db.session.commit()
    return {"success": "UserCourse berhasil dihapus."}, 200
