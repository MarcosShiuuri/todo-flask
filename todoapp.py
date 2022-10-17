from flask import Flask, render_template as rt, request, redirect
from flask_sqlalchemy import SQLAlchemy as sql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_flask.db'
db = sql(app)

@app.route('/', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        print(request.form['task_name'])
        redirect('/')
    else:
        return rt('index.html')