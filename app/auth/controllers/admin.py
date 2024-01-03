import datetime
from flask import jsonify, request
from flask_restful import Resource
from app import app, db
from app.md.models import User
import jwt

class SignUpView(Resource):
    def post(self):
        email = request.json['email']
        username = request.json['username']
        password = request.json['password']

        my_post = User(email=email, username=username, password=password)
        db.session.add(my_post)
        db.session.commit()
        
        return jsonify({"msg": "User Created Successful"})

class LoginView(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']

        post = User.query.filter_by(email=email).first()

        if not post or post.password != password:
            return jsonify({"msg": "Invalid credentials"}), 401

        token = jwt.encode(
            {'user_id': post.id,
             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120)},
            app.config['SECRET_KEY']
        )
        return jsonify({'token': token})

class LogOutView(Resource):
    pass 
