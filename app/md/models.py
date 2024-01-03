from app import db
from sqlalchemy.sql import func
from marshmallow import Schema, fields


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    notes = db.relationship('Note', backref='user', lazy=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    email = fields.Str()
    join_date = fields.Date(dump_only=True)

class NotesSchema(Schema):
    id = fields.Int(dump_only=True)
    data = fields.Str()
    date = fields.DateTime(dump_only=True)
    user_id = fields.Int(dump_only=True)
