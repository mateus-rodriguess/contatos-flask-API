import os

from config import conf
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):
    """
    app creation and api routes
    """
    app = Flask(__name__)
    app.config.from_object(conf[config_name])
    
    api = Api(app, prefix="/api/v1")
    db.init_app(app)
    
    from app.resources.contacts import Contacts
    # rota de contatos
    api.add_resource(Contacts, "/contacts")

    from app.resources.auth import Login, Register
    # rotas de registro e login
    api.add_resource(Login, "/login")
    api.add_resource(Register, "/register")

    return app
    