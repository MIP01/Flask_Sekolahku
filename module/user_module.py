from model import db, User
from sqlalchemy.exc import IntegrityError

def create_user(data):
    try:
        user = User(
            nama=data['nama'],
            email=data['email'],
            no_telp=data['no_telp'])

        db.session.add(user)
        db.session.commit()

        return {"success": "Berhasil membuat user", "data": user.to_dict()}, 200

    except IntegrityError:
        db.session.rollback()  # Rollback untuk membersihkan sesi
        return {"error": "No HP sudah terdaftar. Silakan gunakan No HP lain."}, 409

def get_all_user():
    user_list = User.query.all()

    if not user_list:
        return {'error': 'Tidak ada data yang ditampilkan'}, 404

    # Gunakan to_dict() untuk setiap user
    result = [user.to_dict() for user in user_list]
    
    return result, 200

def get_user_by(user_id):
    user = User.query.get(user_id)

    if not user:
        return {"error": "User tidak ditemukan."}, 404

    return user.to_dict(), 200

def update_user(user_id, data):
    user = User.query.get(user_id)

    if not user:
        return {"error": "User tidak ditemukan."}, 404

    user.nama = data['nama']
    user.email = data['email']
    user.no_telp = data['no_telp']
    db.session.commit()

    return {"success": "Data user berhasil diperbaharui", "data": user.to_dict()}, 200

def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return {"error": "User tidak ditemukan."}, 404

    db.session.delete(user)
    db.session.commit()
    return {"success": "User berhasil dihapus."}, 200
