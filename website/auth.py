from flask import Blueprint, render_template
print("[auth]")

# This will be imported by '__init__.py'
auth = Blueprint('auth', __name__)
print("[auth]: created 'Blueprint('auth')'")

@auth.route('/login')
def login():
    print("[auth]: @auth.route(/login)")
    # 'text' is a variable (chosen by me), not an default parameter. Is passed to 'login.html'
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    print("[auth]: @auth.route(/logout)")
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    print("[auth]: @auth.route(/sign-up)")
    return render_template("sign_up.html")
