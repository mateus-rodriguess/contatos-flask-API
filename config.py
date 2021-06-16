
class Config:
    SECRET_KEY = "SECRET"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost:5432/flask_contacts"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    Debug = True
   

class Testing(Config):
    pass


conf = {
    "devolopment": Development,
    "testing": Testing,
}