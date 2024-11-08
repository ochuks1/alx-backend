#!/usr/bin/env python3
"""
Flask application that uses a user's preferred locale for rendering.
This version integrates locale selection based on URL, user settings, and request headers.
"""

from flask import Flask, request, g, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

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
    """Before each request, set the current user as a global variable."""
    g.user = get_user()

@babel.localeselector
def get_locale():
    """
    Determines the locale to use based on the URL parameters, user settings, or request headers.
    Locale priority:
        1. URL parameter
        2. User settings
        3. Request header
        4. Default to 'en'
    """
    locale = request.args.get('locale')
    if not locale and g.user:
        locale = g.user.get('locale')
    if not locale:
        locale = request.accept_languages.best_match(['en', 'fr'])
    return locale or 'en'

@app.route('/')
def index():
    """Renders the homepage using the selected locale."""
    return render_template('6-index.html')
