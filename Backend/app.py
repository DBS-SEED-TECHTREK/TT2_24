from flask import Flask, jsonify
import json
import requests
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

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

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True) # mac
    app.run(host='localhost', port=5000, debug=True) # windows