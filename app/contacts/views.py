from . import contacts
from flask import render_template, url_for
from app.models import Contact


@contacts.route("/contacts")
def contacts():
    contacts =  Contact.query.all()
    return render_template("contacts/contacts.html", contacts=contacts)



