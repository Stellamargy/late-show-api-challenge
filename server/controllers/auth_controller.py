from flask import Blueprint,request,jsonify
from server.models import User
from server import db
from server.utilis import create_jwt,decode_jwt

auth_bp=Blueprint('auth',__name__,url_prefix='/auth')

@auth_bp.route('/register',methods=['POST'])
def register_user():
    username=request.json['username']
    password=request.json['password']
    if not password or not username:
        return jsonify({'error':'username and  password fields required'}),400
    #Check for existing user
    existing_user=User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error':"Username already exists"}),409
    
    user=User(username=username,password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message':'account created successfully'}),201

@auth_bp.route('/login',methods=['POST'])
def login():
    username=request.json['username']
    password=request.json['password']
    if not username or not password:
        return jsonify({'error': 'Username and password are required fields'}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not user.verify_password(password):
        return jsonify({'error': 'Invalid username or password'}), 401

    token = create_jwt(user)

    return jsonify({
        'access_token': token,
        'message': 'Logged in successfully'
    }), 200

    
    