from model import db, Administrator
from sqlalchemy.exc import IntegrityError

def create_admin(data):
    try:
        admin = Administrator(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        db.session.add(admin)
        db.session.commit()

        return {"success": "Berhasil membuat admin", "data": admin.to_dict()}, 201

    except IntegrityError:
        db.session.rollback()  # Rollback untuk membersihkan sesi
        return {"error": "Email sudah terdaftar. Silakan gunakan Email lain."}, 409

def get_all_admin():
    user_list = Administrator.query.all()

    if not user_list:
        return {'error': 'Tidak ada data yang ditampilkan'}, 404

    # Gunakan to_dict() untuk setiap admin
    result = [admin.to_dict() for admin in user_list]
    
    return result, 200

def get_admin_by(administrator_id, current_user):
    admin = Administrator.query.get(administrator_id)

    if not admin:
        return {"error": "Administrator tidak ditemukan."}, 404

    # Verifikasi bahwa admin yang sedang login hanya bisa menghapus dirinya sendiri
    if current_user['role'] == 'administrator' and admin.administrator_id != current_user['id']:
        return {'error': 'Unauthorized access to this admin'}, 403

    return admin.to_dict(), 200

def update_admin(administrator_id, data, current_user):
    admin = Administrator.query.get(administrator_id)

    if not admin:
        return {"error": "Administrator tidak ditemukan."}, 404

    # Verifikasi bahwa admin yang sedang login hanya bisa mengupdate dirinya sendiri
    if current_user['role'] == 'administrator' and admin.administrator_id != current_user['id']:
        return {'error': 'Unauthorized access to update this admin'}, 403

    admin.username = data['username']
    admin.email = data['email']
    admin.password = data['password']
    db.session.commit()

    return {"success": "Data admin berhasil diperbaharui", "data": admin.to_dict()}, 200

def delete_admin(administrator_id, current_user):
    admin = Administrator.query.get(administrator_id)

    if not admin:
        return {"error": "Administrator tidak ditemukan."}, 404

     # Verifikasi bahwa admin yang sedang login hanya bisa menghapus dirinya sendiri
    if current_user['role'] == 'administrator' and admin.administrator_id != current_user['id']:
        return {'error': 'Unauthorized access to delete this admin'}, 403

    db.session.delete(admin)
    db.session.commit()
    return {"success": "Administrator berhasil dihapus."}, 200
