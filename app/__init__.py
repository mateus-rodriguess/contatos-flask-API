from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import conf

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()


def create_app(config_name):
    """
    app creation and api routes
    """
    app = Flask(__name__)
    app.config.from_object(conf[config_name])
    
    api = Api(app, prefix="/api/v1")
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    
    from app.api.resources.contacts import Contacts

    api.add_resource(Contacts, "/contacts")

    from app.api.resources.auth import Login, Register

    api.add_resource(Login, "/login")
    api.add_resource(Register, "/register")

    from app import routes
    routes.init_app(app)

    return app
    