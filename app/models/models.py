from app import db
from sqlalchemy import ForeignKey
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    correo = db.Column(db.String(150), unique=False, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    posts = db.relationship('Post')
    coments = db.relationship('Coment')

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150),nullable=False)
    content = db.Column(db.String(255),nullable=False)
    fechacreacion=db.Column(db.DateTime, default=datetime.utcnow)
    user = db.Column(
        db.Integer,
        ForeignKey('user.id'),
        nullable=False,
    )
    category = db.Column(
        db.Integer,
        ForeignKey('category.id'),
        nullable=False,
    )
    user_obj = db.relationship('User')
    category_obj = db.relationship('Category')

class Coment(db.Model):
    __tablename__ = 'coment'

    id = db.Column(db.Integer, primary_key=True)
    coment = db.Column(db.String(150),nullable=False)
    fechacreacion=db.Column(db.DateTime, default=datetime.utcnow)
    user = db.Column(
        db.Integer,
        ForeignKey('user.id'),
        nullable=False,
    )
    post = db.Column(
        db.Integer,
        ForeignKey('post.id'),
        nullable=False,
    )
    user_obj = db.relationship('User')
    post_obj = db.relationship('Post')

class Category(db.Model):
    __tablename__="category"

    id = db.Column(db.Integer, primary_key=True)
    etiqueta = db.Column(db.String(150), unique=True, nullable=False)
    posts = db.relationship('Post')