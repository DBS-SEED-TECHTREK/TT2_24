from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/login', methods=['GET'])
def login():
    username = request.authorization.username
    password = request.authorization.password

    # CHECK USERNAME & PASSWORD

    # CREATE TOKEN

    return Response(status=201)

