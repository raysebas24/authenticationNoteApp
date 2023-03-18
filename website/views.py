from flask import Blueprint, render_template
print("[views]")

# This will be imported by '__init__.py'
views = Blueprint('views', __name__)
print("[views]: created 'Blueprint('views')")

@views.route('/')
def home():
    print("[views]: @views.route(/)")
    return render_template("home.html")

