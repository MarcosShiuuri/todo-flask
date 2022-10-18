from flask import Flask, render_template as rt, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_flask.db'
db = SQLAlchemy(app)
db.init_app(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    def __repr__(self):
        return '<Task %r>' % self.id
with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        print(request.form['task_name'])
        return redirect('/')
    else:
        return rt('index.html')