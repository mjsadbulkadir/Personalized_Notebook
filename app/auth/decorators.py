from functools import wraps
from app import app
from flask import jsonify, request
import jwt

from app.md.models import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        
        if not token:
            return jsonify({'message': 'Token is missing!'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"], options=None)
            current_user = User.query.filter_by(id=data['user_id']).first()
            if 'user_id' not in data or current_user.id != data["user_id"]:
                return jsonify({'message': 'Token is invalid or does not match session!'})
        
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token is expired!'})
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'})

        return f(current_user)

    return decorated
