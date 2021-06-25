from flask import render_template, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_required, login_user, logout_user
from app.models import User
from app.forms import LoginForm, RegisterForm
from app import db

from . import auth


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        
        user = User.query.filter_by(username=form.user_name.data).first()

        if not user:
            return redirect(url_for("auth.login"))

        if not user or not user.compare_password(form.password.data):
            return redirect(url_for("auth.login"))

        login_user(user)
        return redirect(url_for("contacts.contacts"))

    return render_template("auth/login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
       
        username = form.user_name.data
        password = form.password.data
        email = form.email.data
        
        user = User(username, password, email)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for("contacts.contacts"))
    return render_template("auth/register.html", form=form)