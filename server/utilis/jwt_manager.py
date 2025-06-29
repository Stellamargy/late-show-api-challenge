import jwt
from flask import current_app

# Create JWT token
def create_jwt(user):
    payload = {
        'id': user.id,
        'username': user.username
    }
    return jwt.encode(payload=payload, key=current_app.config['SECRET_KEY'], algorithm='HS256')

# Decode JWT
def decode_jwt(token):
    return jwt.decode(token, key=current_app.config['SECRET_KEY'], algorithms=['HS256'])

