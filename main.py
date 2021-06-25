from app import create_app, db
from flask_migrate import Migrate
from app.models import User, Contact

app = create_app("devolopment")

Migrate(app, db)


@app.shell_context_processor
def shell_context():
    return dict(
        app=app,
        db=db,
        User=User,
        Contact=Contact,
    )


if __name__ == "__main__":
    app.run(debug=True)

    

