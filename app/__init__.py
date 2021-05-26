from flask import Flask
from flask_sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
flask_app.config.from_object('config.flask_config')
db = SQLAlchemy(flask_app)


def setup_db():
    # Import models here

    db.create_all()


def get_register_blueprints():
    # Import blueprints here
    return [

    ]
