# stores the standard routes of the websites
from flask import Blueprint

# This will be imported by '__init__.py'
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"

