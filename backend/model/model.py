from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    passward = db.Column(db.String(10), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_data = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class Users_names(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    created_data = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class Users_password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    passward = db.Column(db.String(15), nullable=False)
    created_data = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class Users_status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    old = db.Column(db.Integer, nullable=False)
    created_data= db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class Creates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10), nullable=False)
    img = db.Column(db.String(10), nullable=False)
    comment = db.Column(db.String(20), nullable=False)
    goodcount = db.Column(db.String(50), nullable=False)
    created_data= db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class Creates_title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10), nullable=False)
    content = db.Column(db.String(300), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class Creates_img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imgpath = db.VARCHAR(db.String(100))
    created_data= db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class Creates_goodcount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supporter_id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, primary_key=True)
    created_data= db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class Creates_comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    supporter_id = db.Column(db.Integer, primary_key=True)
    supporter_name = db.Column(db.String(10), nullable=False)
    supporter_content = db.Column(db.String(100), nullable=False)
    created_data= db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

db.create_all()

admin = Admin()
admin.add_view(ModelView(Users,db.session))
admin.add_view(ModelView(Users_names,db.session))
admin.add_view(ModelView(Users_password,db.session))
admin.add_view(ModelView(Users_status,db.session))
admin.add_view(ModelView(Creates,db.session))
admin.add_view(ModelView(Creates_title,db.session))
admin.add_view(ModelView(Creates_img,db.session))
admin.add_view(ModelView(Creates_goodcount,db.session))
admin.add_view(ModelView(Creates_comment,db.session))

