from flask import (
    Blueprint,
    render_template,
    url_for,
    redirect,
    flash,
    request
    )

from ..models import Task
from ..extensions import db

edit_bp = Blueprint('edit', __name__)

@edit_bp.route('/todo/<int:id>/edit')
def render_edit(id):

    task = Task.query.filter_by(id=id).one()

    return render_template('edit.html', task=task)


@edit_bp.route('/edit/<int:id>/', methods=['GET', 'POST'])
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
            return redirect(url_for('index.main'))

    return render_template('edit.html', task=task)