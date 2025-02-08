from flask import Blueprint, request, jsonify
from app import db
from app.models import User, Task
from flask_jwt_extended import create_access_token

api = Blueprint('api', __name__)

@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered!"}), 201

@api.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title, "due_date": t.due_date} for t in tasks])