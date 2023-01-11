from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seat = db.Column(db.String(10000))
    passenger = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    flight = db.relationship('Flight')

