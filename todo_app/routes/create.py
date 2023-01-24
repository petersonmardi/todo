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

create_bp = Blueprint('create', __name__)

@create_bp.route('/todo/add', methods=['GET', 'POST'])
def add():

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
            return redirect(url_for('index.main'))

    return render_template('index.html')