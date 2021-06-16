from flask_restful import fields


contact_filds = {
    "id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "cellphone": fields.String,
}

user_fields = {
    "username": fields.String,
    "email": fields.String,
}