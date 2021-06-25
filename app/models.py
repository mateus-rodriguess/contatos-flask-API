from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def current_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True, index=True)
    
    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        
    def compare_password(self, password):
        return check_password_hash(self.password,  password)
    
    def __repr__(self):
        return f"<User: {self.username}, <Email: {self.email}"
        
    
class Contact(db.Model):
    __tablename__ = "contacts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(35)) 
    last_name = db.Column(db.String(35))
    cellphone = db.Column(db.String(15), nullable=True, unique=True)
    
    def __init__(self, first_name, last_name, cellphone):
        self.first_name = first_name
        self.last_name = last_name
        self.cellphone = cellphone
