from app.auth import auth as auth_blueprint
from app.contacts import contacts as contacts_blueprint


def init_app(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(contacts_blueprint)

