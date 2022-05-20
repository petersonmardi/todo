from flask import Flask
from .extensions import db, migrate
from .credentials import *
import os

def create_app():

    random_key = os.urandom(16)

    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=random_key,
        #SQLALCHEMY_DATABASE_URI=r'sqlite:///C:\Users\pc\Documents\MyWorkSpace\todo\instance\database\1\my_app.db',
        SQLALCHEMY_DATABASE_URI=f"postgresql://{username}:{password}@localhost:1167/{database}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/todo')
    def test():
        return "Testing my todo app..."

    from . import todo
    app.register_blueprint(todo.bp)

    return app

db.create_all(app=create_app())
