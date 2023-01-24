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

bp = Blueprint('index', __name__)


@bp.route('/')
def main():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)