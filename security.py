import jwt
from functools import wraps
from flask import Blueprint, request, make_response, current_app, jsonify
from werkzeug.security import check_password_hash
from app.db import userz
from datetime import datetime, timezone, timedelta


bp = Blueprint('security', __name__)


@bp.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    error = None

    try:
        user = userz[username]
    except:
        user = None

    if user is None or not check_password_hash(user['password'], password):
        error = 'Incorrect user or password'

    if error is None:
        payload = {
            'iat': datetime.now(timezone.utc),                          # Current time
            'exp': datetime.now(timezone.utc) + timedelta(minutes=1),  # Expiration time
            'sub': user['name'],
            'rol': user['rol']
        }
        token = {"token": jwt.encode(payload, current_app.config['SECRET_KEY'],algorithm='HS256')}
        return token, 200

    return make_response(jsonify({'error:': error}), 401)


def token_required(rol):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')

            if not token:
                return make_response(jsonify({'error': 'No token'}), 401)
            
            try:
                data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            except:
                return make_response(jsonify({'error': 'Invalid credentials'}), 401)
            
            if rol != data['rol']:
                return make_response(jsonify({'error': 'Invalid role'}), 403)

            return f(*args, **kwargs)
        return decorated

    return decorator
