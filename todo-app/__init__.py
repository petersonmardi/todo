from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=False)

    key_value = []
    random_key = os.urandom(16)
    key_value.append(random_key)

    app.config.from_mapping(
        SECRET_KEY=key_value[0],
        SQLALCHEMY_DATABASE_URI="sqlite:///instance/database/1/db.sqlite3",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    @app.route('/todo')
    def test():
        return "Testing my todo app..."

    from . import todo
    app.register_blueprint(todo.bp)

    return app
    return app
