#!/usr/bin/env python3
"""
Flask application that handles user time zone preferences and uses the pytz library
to ensure valid time zones are used.
"""

from flask import Flask, request, g, render_template
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user() -> dict:
    """Retrieve user based on the 'login_as' URL parameter."""
    user_id = request.args.get("login_as")
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None

@app.before_request
def before_request():
    """Set the current user globally for each request."""
    g.user = get_user()

@babel.timezoneselector
def get_timezone():
    """
    Determines the user's time zone preference.
    Priority: URL parameter > User settings > UTC (default).
    Validates the time zone using pytz.
    """
    timezone = request.args.get('timezone')
    if not timezone and g.user:
        timezone = g.user.get('timezone')
    try:
        return pytz.timezone(timezone) if timezone else pytz.UTC
    except UnknownTimeZoneError:
        return pytz.UTC

@app.route('/')
def index():
    """Renders the homepage, showing current time based on user time zone."""
    from datetime import datetime
    current_time = datetime.now(get_timezone())
    return render_template('7-index.html', current_time=current_time)
