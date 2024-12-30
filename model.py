from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    _nama = db.Column(db.String(100), nullable=False, unique=True)
    _email = db.Column(db.String(150), nullable=False, unique=True)
    no_telp = db.Column(db.String(18), unique=True, nullable=False)

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, value):
        self._nama = value.upper()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value.upper()

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'nama': self.nama,
            'email': self.email,
            'no_telp' : self.no_telp,
        }
