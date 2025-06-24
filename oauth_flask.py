from flask import Flask, redirect, url_for, session, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
import jwt
from datetime import datetime, timedelta
from models import db, User, Project, ActivityLog

app = Flask(__name__)
app.secret_key = 'pakai_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pakai.db'
CORS(app)
db.init_app(app)

oauth = OAuth(app)
# Google OAuth config (آپ کو client_id اور client_secret اپنی Google Cloud سے لینا ہوں گے)
app.config['GOOGLE_CLIENT_ID'] = 'YOUR_GOOGLE_CLIENT_ID'
app.config['GOOGLE_CLIENT_SECRET'] = 'YOUR_GOOGLE_CLIENT_SECRET'
app.config['GITHUB_CLIENT_ID'] = 'YOUR_GITHUB_CLIENT_ID'
app.config['GITHUB_CLIENT_SECRET'] = 'YOUR_GITHUB_CLIENT_SECRET'

google = oauth.register(
    name='google',
    client_id=app.config['GOOGLE_CLIENT_ID'],
    client_secret=app.config['GOOGLE_CLIENT_SECRET'],
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    client_kwargs={'scope': 'openid email profile'},
)

github = oauth.register(
    name='github',
    client_id=app.config['GITHUB_CLIENT_ID'],
    client_secret=app.config['GITHUB_CLIENT_SECRET'],
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

# JWT helper
JWT_SECRET = 'pakai_jwt_secret'
def generate_jwt(user):
    payload = {
        'user_id': user.id,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')

@app.route('/')
def home():
    return 'Pak AI OAuth Backend Running!'

@app.route('/login/google')
def login_google():
    redirect_uri = url_for('authorize_google', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize/google')
def authorize_google():
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    user_info = resp.json()
    user = User.query.filter_by(email=user_info['email']).first()
    if not user:
        user = User(email=user_info['email'], name=user_info['name'], provider='google')
        db.session.add(user)
        db.session.commit()
    jwt_token = generate_jwt(user)
    return jsonify({'token': jwt_token, 'user': {'name': user.name, 'email': user.email}})

@app.route('/login/github')
def login_github():
    redirect_uri = url_for('authorize_github', _external=True)
    return github.authorize_redirect(redirect_uri)

@app.route('/authorize/github')
def authorize_github():
    token = github.authorize_access_token()
    resp = github.get('user')
    user_info = resp.json()
    email = user_info.get('email') or user_info.get('login')
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email, name=user_info.get('name') or email, provider='github')
        db.session.add(user)
        db.session.commit()
    jwt_token = generate_jwt(user)
    return jsonify({'token': jwt_token, 'user': {'name': user.name, 'email': user.email}})

@app.route('/user', methods=['GET'])
def get_user():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = User.query.get(payload['user_id'])
        return jsonify({'name': user.name, 'email': user.email, 'credits': user.credits})
    except Exception as e:
        return jsonify({'error': str(e)}), 401

@app.route('/projects', methods=['GET'])
def get_projects():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = User.query.get(payload['user_id'])
        projects = Project.query.filter_by(user_id=user.id).all()
        return jsonify([{'name': p.name, 'privacy': p.privacy, 'created_at': p.created_at, 'thumb_url': p.thumb_url, 'file_url': p.file_url} for p in projects])
    except Exception as e:
        return jsonify({'error': str(e)}), 401

@app.route('/analytics', methods=['GET'])
def get_analytics():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = User.query.get(payload['user_id'])
        # ڈیمو اینالیٹکس
        return jsonify({'credits_used': 12, 'credits_total': user.credits, 'last_login': str(user.created_at), 'feature_usage': {'Text to Image': 5, 'Text to Voice': 3, 'Video': 2}})
    except Exception as e:
        return jsonify({'error': str(e)}), 401

@app.route('/activity', methods=['GET'])
def get_activity():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = User.query.get(payload['user_id'])
        logs = ActivityLog.query.filter_by(user_id=user.id).order_by(ActivityLog.timestamp.desc()).limit(20).all()
        return jsonify([{'action': l.action, 'timestamp': str(l.timestamp)} for l in logs])
    except Exception as e:
        return jsonify({'error': str(e)}), 401

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5001, debug=True) 