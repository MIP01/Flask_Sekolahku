from model import db, User
from sqlalchemy.exc import IntegrityError

def create_user(data):
    try:
        result = User(
            nama=data['nama'],
            alamat=data['alamat'])

        db.session.add(result)
        db.session.commit()

        return {"success": "Berhasil membuat user."}, 200

    except IntegrityError:
        db.session.rollback()  # Rollback untuk membersihkan sesi
        return {'error': 'User sudah ada.'}, 409

def get_users():
    user_list = User.query.all()

    # Membuat list untuk menyimpan hasil yang akan ditampilkan
    result = []

    # Mengiterasi setiap entri mahasiswa dan menyusun dictionary untuk setiap entri
    for user in user_list:
        result.append({
            'user_id': user.user_id,
            'nama': user.nama,
            'alamat': user.alamat
        })
    
    return result

def get_user_by(user_id):
    user = User.query.get(user_id)

    if not user:
        return {"error": "User tidak ditemukan."}, 404

    result = {
        'user_id': user.user_id,
        "nama": user.nama,
        "alamat": user.alamat
    }

    return result

def update_user(user_id, data):
    user = User.query.get(user_id)

    if not user:
        return {"error": "User tidak ditemukan."}, 404

    user.nama = data['nama']
    user.alamat = data['alamat']
    db.session.commit()

    return {"success": "Data user berhasil diperbaharui."}, 200

def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return {"error": "User tidak ditemukan."}, 404

    db.session.delete(user)
    db.session.commit()
    return {"success": "User berhasil dihapus."}, 200
