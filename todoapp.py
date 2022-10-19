from flask import Flask, render_template as rt, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_flask.db'
db = SQLAlchemy(app)
db.init_app(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id
with app.app_context():
    db.create_all()

@app.route('/', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        task_content = request.form.get('task_content')
        new_task = Task(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Deu para adicionar não!'
    else:
        tasks = Task.query.order_by(Task.id).all()
        return rt('index.html', tasks=tasks)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form.get('task_content')
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Deu pra atualizar não!'

    else:
        return rt('update.html', task=task)
 
@app.route('/delete/<int:id>')
def delete(id):
    task_delete = Task.query.get_or_404(id)
    try:
        db.session.delete(task_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Deu pra deletar não!'