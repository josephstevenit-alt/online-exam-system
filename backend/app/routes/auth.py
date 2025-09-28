from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

# 🔑 Create Blueprint first
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"msg":"email and password required"}),400
    if User.query.filter_by(email=email).first():
        return jsonify({"msg":"email already registered"}),400

    user = User(name=name, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg":"registered"}),201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"msg":"invalid credentials"}),401

    # 🔑 Fix: convert user.id to string
    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "access_token": access_token,
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name
        }
    }),200
