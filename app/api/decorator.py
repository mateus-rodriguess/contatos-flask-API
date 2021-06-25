from functools import wraps
from flask_restful import request
import jwt
from flask import current_app
from app.models import User


def jwt_required(f):
    """
    Decorator function for user token validation
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "authorization" in request.headers:
            token = request.headers["authorization"]

        if not token:
            return {"error": "Você não tem permissão para acessar essa rota, você precisa de um token de autenticação"}, 401

        try:
            decoded = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.get(decoded["id"])
        except:
            return {"error": "O token é invalido."}, 403

        return f(current_user=current_user, *args, **kwargs)

    return decorated