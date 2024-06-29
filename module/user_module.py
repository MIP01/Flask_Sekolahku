from model import db, User
from middleware.error_handler import ResourceNotFoundError

def create_user(data):
    new_user = User(name=data['name'], email=data['email'], address=data['address'])
    db.session.add(new_user)
    db.session.commit()
    return new_user.to_dict()

def get_users():
    users = User.query.all()
    return [user.to_dict() for user in users]

def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return user.to_dict()

def update_user(user_id, data):
    user = User.query.get_or_404(user_id)
    user.name = data['name']
    user.email = data['email']
    user.address = data['address']
    db.session.commit()
    return user.to_dict()

def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return 'Data Deleted'
