#!/usr/bin/env python3
"""
Flask application to handle user login and localization.
The application mocks a user login system and renders messages in different languages.
"""

from flask import Flask, request, g, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# Mock user data (mocking a database)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> dict:
    """
    Retrieves the user dictionary based on the 'login_as' URL parameter.
    If no valid user is found, returns None.
    """
    user_id = request.args.get("login_as")
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None

@app.before_request
def before_request():
    """
    Before every request, check for a user and store it in Flask's global g.
    This function is executed before all other functions.
    """
    g.user = get_user()

@app.route('/')
def index():
    """
    Renders the homepage and shows the current login status based on the user.
    Displays either a login message or a default message.
    """
    return render_template('5-index.html')
