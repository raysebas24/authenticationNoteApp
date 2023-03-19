from flask import Blueprint, render_template, request, flash
print("[auth]")

# This will be imported by '__init__.py'
auth = Blueprint('auth', __name__)
print("[auth]: created 'Blueprint('auth')'")

# by default, methods can only handle GET requests
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # gets the data from the HTML page
    #data = request.form
    #print(data)
    print("[auth]: @auth.route(/login)")
    # 'text' is a variable (chosen by me), not an default parameter. Is passed to 'login.html'
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    print("[auth]: @auth.route(/logout)")
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # gets the data from the HTML page
        #email = request.form['email']
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        passwort1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif passwort1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(passwort1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')
    print("[auth]: @auth.route(/sign-up)")
    return render_template("sign_up.html")
