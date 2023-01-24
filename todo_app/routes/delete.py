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

delete_bp = Blueprint('delete', __name__)


@delete_bp.route('/todo/delete/<int:id>/')
def delete(id):
    get_task = Task.query.filter_by(id=id).one()
    db.session.delete(get_task)
    db.session.commit()
    return redirect(url_for('index.main'))