from flask_wtf import FlaskForm
from wtforms.fields import (PasswordField, StringField, SubmitField)
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    user_name = StringField("User name", validators=[
        DataRequired("Campo obrigatório")])
    password = PasswordField("Senha", validators=[
        Length(4, 40, "O campo deve conter entre 3 á 6 caracters.")
    ])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    user_name = StringField("User name", validators=[
        DataRequired("User name é obrigatório")
    ])
    email = EmailField("Email", validators=[
        Email()
    ])
    password = PasswordField("Senha", validators=[
        Length(4, 40, "O campo deve conter entre 3 á 6 caracters.")
    ])
    submit = SubmitField("Cadastrar")


class ContactForm(FlaskForm):
    first_name = StringField("Primeiro nome", validators=[
        DataRequired("O campo é obrigatório ")
    ])
    last_name = StringField("Segundo nome", validators=[
        DataRequired("O campo e obrigatório ")
    ])
    cellphone = StringField("Numero", validators=[Length(8, 15, "Numero invalido")])

