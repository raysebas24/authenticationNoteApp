from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
print("[__init__]")


db = SQLAlchemy()
DB_NAME = "datebase.db"

def create_app():
    print("[__init__]: inside 'create_app()'")
    app = Flask(__name__)
    print("[__init__]: created 'Flask()'")
    # SECRET_KEY = used for securly signing the session cookie or other security needs
    app.config['SECRET_KEY'] = 'admin'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:admin@localhost/{DB_NAME}'#feedback_mercedes'
    db.init_app(app)


    # importing 'views' and 'auth' from app 'views.py' and 'auth.py'
    from .views import views
    from .auth import auth

    # with 'url_prefix' another name suffix is expected in the URL
    app.register_blueprint(views, url_prefix='/')
    print("[__init__]: 'views' registered")
    app.register_blueprint(auth, url_prefix='/')
    print("[__init__]: 'auth' registered")

    from .models import User, Note

    create_database(app)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()            
        #db.create_all(app=app)
        print('[__init__]: Created Database!')
