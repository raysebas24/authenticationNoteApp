from flask import Flask
print("[__init__]")

def create_app():
    print("[__init__]: inside 'create_app()'")
    # create an Flask instance
    app = Flask(__name__)
    print("[__init__]: created 'Flask()'")
    # SECRET_KEY = used for securly signing the session cookie or other security needs
    app.config['SECRET_KEY'] = 'abcd1234'

    # importing 'views' and 'auth' from app 'views.py' and 'auth.py'
    from .views import views
    from .auth import auth

    # with 'url_prefix' another name suffix is expected in the URL
    app.register_blueprint(views, url_prefix='/')
    print("[__init__]: 'views' registered")
    app.register_blueprint(auth, url_prefix='/')
    print("[__init__]: 'auth' registered")

    return app

