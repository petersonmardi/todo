from flask import Flask
from .extensions import db, migrate
# from .credentials import *
import os

def create_app():

    random_key = os.urandom(16)

    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=random_key,
        SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        db.create_all()
        print('Initialized database...')

    @app.route('/todo')
    def test():
        return "Testing my todo app..."

    from .routes.index import bp
    app.register_blueprint(bp)
    
    from .routes.create import create_bp
    app.register_blueprint(create_bp)
    
    from .routes.edit import edit_bp
    app.register_blueprint(edit_bp)
    
    from .routes.delete import delete_bp
    app.register_blueprint(delete_bp)

    return app

create_app()
