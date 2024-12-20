from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    _nama = db.Column(db.String(100), nullable=False, unique=True)
    _alamat = db.Column(db.String(150), nullable=False)

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, value):
        self._nama = value.upper()

    @property
    def alamat(self):
        return self._alamat

    @alamat.setter
    def alamat(self, value):
        self._alamat = value.upper()

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'nama': self.nama,
            'alamat': self.alamat,
        }
