from flask_restful import Resource, marshal, request
from app.models import User
from app import db
from app.api.schemas.schemas import user_fields
import jwt
import datetime
from flask import current_app


class Login(Resource):
    
    def post(self):
        credential = request.get_json(force=True)
        user = User.query.filter_by(username=credential["username"]).first()
        
        if not user or not user.compare_password(credential["password"]):
            return {"error": "Credenciais inválida."}, 400

        data = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=23)
        }
        
        try:
            token = jwt.encode(data, current_app.config["SECRET_KEY"])
            return {"access_token": token.encode().decode("utf-8")}

        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500


class Register(Resource):
    
    def post(self):
        payload = request.get_json(force=True)

        try:
            username = payload["username"]
            password = payload["password"]
            email = payload["email"]
           
            user = User(username, password, email)

            db.session.add(user)
            db.session.commit()
            return marshal(user, user_fields, "user")

        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500




