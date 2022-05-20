from flask import Flask
from .extensions import db, migrate
import os

def create_app():
    credentials = ("postgres", "k4t4r.167", "todo_db") #postgresql username, password, dbname
    random_key = os.urandom(16)

    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=random_key,
        #SQLALCHEMY_DATABASE_URI=r'sqlite:///C:\Users\pc\Documents\MyWorkSpace\todo\instance\database\1\my_app.db',
        SQLALCHEMY_DATABASE_URI="postgresql://postgres:k4t4r.167@localhost:1167/postgres",
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
