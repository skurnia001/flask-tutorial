from flask import Flask
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
flask_app.config.from_object('config.flask_config')
db = SQLAlchemy(flask_app)


def setup_db():
    # Import models here
    from app.model import book_model

    db.create_all()


def get_register_blueprints():
    # Import blueprints here
    from app.view.book_view import book_blueprint

    return [
        book_blueprint
    ]


setup_db()

[flask_app.register_blueprint(blueprint) for blueprint in get_register_blueprints()]
