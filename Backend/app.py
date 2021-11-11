from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from flask import Flask, jsonify
from flask import request
from flask import Response
import json
import requests
from datetime import datetime, timedelta, timezone
import jwt
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATION


app = Flask(__name__)

# CORS
CORS(app)

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = SQLALCHEMY_TRACK_MODIFICATION
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

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    name = db.Column(db.String())
    description = db.Column(db.String())
    amount = db.Column(db.Integer)
    created_at = db.Column(db.String())
    created_by = db.Column(db.DateTime)
    updated_at = db.Column(db.String())
    updated_by = db.Column(db.DateTime())
    
    
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


#######################
## AUTHORIZATION & AUTHENTICATION
#######################
def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
       if 'x-access-tokens' in request.headers:
           token = request.headers['x-access-tokens']
 
       if not token:
           return jsonify({'message': 'a valid token is missing'})
       try:
           print("token: ", token)
           data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
           print("data[id]: ", data['id'])
           current_user = user_db.query.filter_by(id=data['id']).first()
       except:
           return jsonify({'message': 'token is invalid'})
 
       return f(current_user, *args, **kwargs)
   return decorator


@app.route('/api/login', methods=['POST'])
def login():
    request_data = request.get_json()

    input_username = request_data['username']
    input_password = request_data['password']

    # CHECK USERNAME & PASSWORD
    user = user_db.query.filter_by(username=input_username).first()  
    
    if user.password == input_password:
        token = jwt.encode({'id' : user.id, 'exp' : datetime.utcnow() + timedelta(minutes=60)}, SECRET_KEY, "HS256")
        return jsonify({'token' : token})

    return jsonify({'message': 'credentials are invalid'}), 401


#######################
## USERS
#######################

# Get all Users
@app.route('/api/get_users', methods=['POST'])
def get_users():
    result = []
    for user in user_db.query.all():
        result.append(user.json())
    return jsonify({"type": "success", "users": result}), 200


#######################
## PROJECTS
#######################

# Get all project
@app.route('/api/get_projects', methods=['POST'])
def get_projects():
    result = []
    for project in project_db.query.all():
        result.append(project.json())
    return jsonify({"type": "success", "project": result}), 200


# get_projects_by_user
@app.route('/api/get_projects_by_user_id', methods=['POST'])
@token_required
def get_projects_by_user_id(current_user):
    user_id = current_user.id
    result = []
    for project in project_db.query.filter_by(user_id=user_id).all():
        result.append(project.json())
    return jsonify({"type": "success", "project": result}), 200


#######################
## EXPENSES
#######################
    
# create expense by project
@app.route('/api/add_expense', methods=['POST'])
@token_required
def add_expense(current_user):
    data = request.get_json()
    expense_info = expense_db(**data)
    id = current_user.id
    existing_expense = expense_db.query.filter_by(id=id).one_or_none()
    if existing_expense is None:
        #expense = expense_db(id,project_id,category_id,name,description,amount,created_at,created_by,updated_at,updated_by)
        db.session.add(expense_info)
        db.session.commit()
    result = []
    for expense in expense_db.query.filter_by(id=id).all():
        result.append(expense.json())
    return jsonify({"type": "success", "project": result}), 200


# get expense by project
@app.route('/api/get_expense', methods=['POST'])
@token_required
def get_expense(current_user):
    data = request.get_json()
    id = data['id']
    result = []
    for expense in expense_db.query.filter_by(project_id=id).all():
        result.append(expense.json())
    return jsonify({"type": "success", "project": result}), 200


# update expense by project
@app.route('/api/update_expense', methods=['PUT'])
@token_required
def update_expense(current_user):
    data = request.get_json()
    expense_info = expense_db(**data)
    id = data['id']
    project_id = request.json['project_id']
    category_id = request.json['category_id']
    name = request.json['name']
    description = request.json['description']
    amount = request.json['amount']
    created_at = request.json['created_at']
    created_by = request.json['created_by']
    updated_at = request.json['updated_at']
    updated_by = request.json['updated_by']
    
    expense_info = expense_db.query.get_or_404(int(id))
    expense_info.project_id = project_id;
    expense_info.category_id = category_id;
    expense_info.name = name;
    expense_info.description = description;
    expense_info.amount = amount;
    expense_info.created_at = created_at;
    expense_info.created_by = created_by;
    expense_info.updated_at = updated_at;
    expense_info.updated_by = updated_by;

    db.session.commit()
    result = []
    for expense in expense_db.query.filter_by(id=id).all():
        result.append(expense.json())
    return jsonify({"type": "success", "project": result}), 200


# delete expense by project
@app.route('/api/delete_expense', methods = ['DELETE'])
@token_required
def delete_expense(current_user):
    data = request.get_json()
    id = data['id']
    expense_info = expense_db.query.get(int(id))
    
    if expense_info is None:
        return "Expense Not Deleted Successfully", 200
    else:
        db.session.delete(expense_info)
        db.session.commit()
        return "Expense Deleted Successfully", 200


#######################
## CATEGORIES
#######################
@app.route('/api/get_categories', methods=['POST'])
def get_categories():
    result = []
    for category in category_db.query.all():
        result.append(category.json())
    return jsonify({"type": "success", "category": result}), 200


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True) # mac
    app.run(host='localhost', port=5000, debug=True) # windows