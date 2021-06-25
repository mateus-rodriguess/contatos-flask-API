from flask_restful import Resource, marshal
from app.models import Contact
from app import db
from app.api.schemas.schemas import contact_filds
from app.api.decorator import jwt_required
from flask_restful import request


class Contacts(Resource):

    def get(self):
        contacts = Contact.query.all()
        return marshal(contacts, contact_filds, "contacts")

    @jwt_required
    def post(self, current_user):
        payload = request.get_json(force=True)

        first_name = payload["first_name"]
        last_name = payload["last_name"]
        cellphone = payload["cellphone"]

        try:
            contact = Contact(first_name, last_name, cellphone)
            db.session.add(contact)
            db.session.commit()
            return marshal(contact, contact_filds, "contact")
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500

    @jwt_required
    def put(self, current_user):
        payload = request.get_json(force=True)
        _id = payload["id"]
        first_name = payload["first_name"]
        last_name = payload["last_name"]
        cellphone = payload["cellphone"]

        contact = Contact.query.get(_id)

        if not contact:
            return {"message": "Contato não existe."}

        try:
            contact.first_name = first_name
            contact.last_name = last_name
            contact.cellphone = cellphone

            db.session.add(contact)
            db.session.commit()

            return marshal(contact, contact_filds, "contact")
       
        except:
            return {"error": "Houve um problema pra processar o pedido "}

    @jwt_required
    def delete(self, current_user):
        payload = request.get_json(force=True)
        _id = payload["id"]

        contact = Contact.query.get(_id)

        if not contact:
            return {"message": "Contato não existe."}

        try:
            db.session.delete(contact)
            db.session.commit()
            return marshal(contact, contact_filds, "contact")
       
        except:
            return {"error": "Houve um erro ao excluir o contato"}