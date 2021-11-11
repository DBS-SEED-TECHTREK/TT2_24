from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify
from flask import request
from flask import Response
import json
import requests

app = Flask(__name__)

# CORS
CORS(app)

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://admin:dbs_seed_2021@dbs-seed.cq637ugrj1yy.us-east-1.rds.amazonaws.com/project_expenses"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

# Model for Login
class user_db(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    name = db.Column(db.String())
    appointment = db.Column(db.String)

    def __init__(self, id, username, password, name, appointment):
        self.id = id
        self.username = username
        self.password = password
        self.name = name
        self.appointment = appointment
        
    def json(self):
        return {"id": self.id, "username": self.username,"password": self.password, "name": self.name, "appointment": self.appointment}

# Model for Category
class category_db(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())


    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def json(self):
        return {"id": self.id, "name": self.name}

# Model for Project
class project_db(db.Model):
    __tablename__ = "project"

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer())
    name = db.Column(db.String())
    description = db.Column(db.String())
    budget = db.Column(db.String())
    
    def __init__(self, id, user_id, name, description, budget):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.budget = budget
        
    def json(self):
        return {"id": self.id, "user_id": self.user_id,"name": self.name,"description": self.description,"budget": self.budget}

# Model for Project
class expense_db(db.Model):
    __tablename__ = "expense"

    id = db.Column(db.Integer(), primary_key=True)
    project_id = db.Column(db.Integer())
    category_id = db.Column(db.Integer())
    name = db.Column(db.String())
    description = db.Column(db.String())
    amount = db.Column(db.Integer())
    created_at = db.Column(db.String())
    created_by = db.Column(db.String())
    updated_at = db.Column(db.String())
    updated_by = db.Column(db.String())
    
    
    def __init__(self, id, project_id, category_id, name, description,amount, created_at, created_by,updated_at,updated_by):
        self.id = id
        self.project_id = project_id
        self.category_id = category_id
        self.name = name
        self.description = description
        self.amount = amount
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by
        
    def json(self):
        return {"id": self.id, "project_id": self.project_id,"category_id": self.category_id,"name": self.name,"description": self.description,
                "amount": self.amount,"created_at": self.created_at,"created_by": self.created_by,"updated_at": self.updated_at,"updated_by": self.updated_by}


@app.route('/')
def hello():
    return "Hello World!"

# For testing; remove this later
@app.route('/api/get_users', methods=['POST'])
def get_users():
    result = []
    for user in user_db.query.all():
        result.append(user.json())
    return jsonify({"type": "success", "users": result}), 200

@app.route('/api/get_categories', methods=['POST'])
def get_categories():
    result = []
    for category in category_db.query.all():
        result.append(category.json())
    return jsonify({"type": "success", "category": result}), 200


@app.route('/login', methods=['GET'])
def login():
    request_data = request.get_json()

    username = request_data['username']
    password = request_data['password']

    # CHECK USERNAME & PASSWORD

    # CREATE TOKEN

    return Response(status=201)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True) # mac
    app.run(host='localhost', port=5000, debug=True) # windows