from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def index():
    category = request.args.get('category')
    if category:
        tasks = Task.query.filter_by(category=category).order_by(Task.created_at.desc()).all()
    else:
        tasks = Task.query.order_by(Task.created_at.desc()).all()
    categories = db.session.query(Task.category).distinct().all()
    return render_template('index.html', tasks=tasks, categories=[c[0] for c in categories if c[0]])


@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    category = request.form.get('category')
    if title:
        task = Task(title=title, category=category)
        db.session.add(task)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    task = Task.query.get_or_404(task_id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/health')
def health():
    return "OK", 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
