from model import db, User
from sqlalchemy.exc import IntegrityError

def create_user(data):
    try:
        user = User(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        db.session.add(user)
        db.session.commit()

        return {"success": "Berhasil membuat user", "data": user.to_dict()}, 201

    except IntegrityError:
        db.session.rollback()  # Rollback untuk membersihkan sesi
        return {"error": "Email sudah terdaftar. Silakan gunakan Email lain."}, 409

def get_all_user():
    user_list = User.query.all()

    if not user_list:
        return {'error': 'Tidak ada data yang ditampilkan'}, 404

    # Gunakan to_dict() untuk setiap user
    result = [user.to_dict() for user in user_list]
    
    return result, 200

def get_user_by(user_id, current_user):
    user = User.query.get(user_id)

    if not user:
        return {"error": "User tidak ditemukan."}, 404

    # Verifikasi bahwa user yang sedang login hanya bisa menghapus dirinya sendiri
    if current_user['role'] == 'user' and user.user_id != current_user['id']:
        return {'error': 'Unauthorized access to this user'}, 403

    return user.to_dict(), 200

def update_user(user_id, data, current_user):
    user = User.query.get(user_id)

    if not user:
        return {"error": "User tidak ditemukan."}, 404

    # Verifikasi bahwa user yang sedang login hanya bisa mengupdate dirinya sendiri
    if current_user['role'] == 'user' and user.user_id != current_user['id']:
        return {'error': 'Unauthorized access to update this user'}, 403

    user.username = data['username']
    user.email = data['email']
    user.password = data['password']
    db.session.commit()

    return {"success": "Data user berhasil diperbaharui", "data": user.to_dict()}, 200

def delete_user(user_id, current_user):
    user = User.query.get(user_id)

    if not user:
        return {"error": "User tidak ditemukan."}, 404

     # Verifikasi bahwa user yang sedang login hanya bisa menghapus dirinya sendiri
    if current_user['role'] == 'user' and user.user_id != current_user['id']:
        return {'error': 'Unauthorized access to delete this user'}, 403

    db.session.delete(user)
    db.session.commit()
    return {"success": "User berhasil dihapus."}, 200
