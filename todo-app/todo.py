from flask import (
    Blueprint,
    render_template,
    url_for,
    redirect,
    flash,
    request
    )

from .models import Task, db

bp = Blueprint('todo', __name__)


@bp.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@bp.route('/todo/add', methods=['GET', 'POST'])
def add_task():

    if request.method == 'POST':
        error = None

        text = request.form['task']

        if not text:
            error = 'This space cannot be empty.'
        if error is not None:
            flash(error)
        else:
            task = Task(text=text)

            db.session.add(task)
            db.session.commit()
            return redirect(url_for('todo.index'))

    return render_template('index.html')


@bp.route('/todo/<int:id>/edit')
def render_edit(id):

    task = Task.query.filter_by(id=id).one()

    return render_template('edit.html', task=task)


@bp.route('/edit/<int:id>/', methods=['GET', 'POST'])
def edit(id):
    task = Task.query.filter_by(id=id).one()

    if request.method == 'POST':
        error = None

        edit_task = request.form['edit']

        if not edit_task:
            error = 'This space cannot be empty.'

        if error is not None:
            flash(error)
        else:
            task.text = edit_task
            db.session.commit()
            return redirect(url_for('todo.index'))

    return render_template('edit.html', task=task)


@bp.route('/todo/delete/<int:id>/')
def delete(id):
    get_task = Task.query.filter_by(id=id).one()
    db.session.delete(get_task)
    db.session.commit()
    return redirect(url_for('todo.index'))
