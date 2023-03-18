from flask import Blueprint
print("[auth]")

# This will be imported by '__init__.py'
auth = Blueprint('auth', __name__)
print("[auth]: created 'Blueprint('auth')'")

@auth.route('/login')
def login():
    print("[auth]: @auth.route(/login)")
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    print("[auth]: @auth.route(/logout)")
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    print("[auth]: @auth.route(/sign-up)")
    return "<p>Sign-Up</p>"
