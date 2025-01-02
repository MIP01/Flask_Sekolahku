from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from datetime import datetime, timezone

db = SQLAlchemy()

class Administrator(db.Model):
    __tablename__ = 'administrator'

    administrator_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(330), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    role = db.Column(db.String(20), default='administrator')

    def to_dict(self):
        return {
            'administrator_id': self.administrator_id,
            'username': self.username,
            'email' : self.email,
            'password': self.password,
            'created_at' : self.created_at,
            'updated_at': self.updated_at,
        }

class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(330), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    role = db.Column(db.String(20), default='user')

    # Relation to user_course
    user_course = relationship('UserCourse', back_populates='user', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'password' : self.password,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

class Courses(db.Model):
    __tablename__ = 'courses'

    course_id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(100), nullable=False, unique=True)
    mentor = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(30), nullable=False)

    # Relation to transaction
    user_course = relationship('UserCourse', back_populates='courses')

    def to_dict(self):
        return {
            'course_id': self.course_id,
            'course': self.course,
            'mentor': self.mentor,
            'title' : self.title,
        }

class UserCourse(db.Model):
    __tablename__ = 'user_course'

    userCourse_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.user_id'), nullable=False)
    course_id = db.Column(db.Integer, ForeignKey('courses.course_id'), nullable=True)

    # Relation to detail and item
    user = relationship('User', back_populates='user_course')
    courses = relationship('Courses', back_populates='user_course')

    def to_dict(self):
        return {
            'userCourse_id': self.userCourse_id,
            'user_id': self.user_id,
            'course_id': self.course_id,
        }