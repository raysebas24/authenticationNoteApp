from flask import Flask

def create_app():
    app = Flask(__name__)
    # SECRET_KEY = used for securly signing the session cookie or other security needs
    app.config['SECRET_KEY'] = 'abcd1234'

    # importing views and auth from app views.py and auth.py
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

