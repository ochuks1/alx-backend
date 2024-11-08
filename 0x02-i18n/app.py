#!/usr/bin/env python3
"""
Flask application that demonstrates localization (i18n) and time zone management.
"""

from flask import Flask, g, request, render_template
from babel import Locale, dates
from babel.support import Translations
import pytz
from datetime import datetime
import pytz

app = Flask(__name__)

# Mock users
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """ Retrieve the user based on login_as parameter. """
    user_id = request.args.get('login_as', type=int)
    return users.get(user_id)

@app.before_request
def before_request():
    """ Set global user and locale before processing each request. """
    user = get_user()
    if user:
        g.user = user
        g.locale = user['locale'] or 'en'
        g.timezone = user['timezone'] or 'UTC'
    else:
        g.user = None
        g.locale = 'en'
        g.timezone = 'UTC'

def get_locale():
    """ Return the locale to use, prioritized by URL param, user settings, etc. """
    return g.locale

def get_timezone():
    """ Return the timezone to use, prioritized by URL param, user settings, etc. """
    try:
        return pytz.timezone(g.timezone)
    except pytz.UnknownTimeZoneError:
        return pytz.UTC

@app.route('/')
def index():
    """ Main route to display the current time based on user time zone. """
    tz = get_timezone()
    current_time = datetime.now(tz)
    current_time_formatted = dates.format_datetime(current_time, locale=g.locale)
    return render_template('index.html', current_time=current_time_formatted)

if __name__ == "__main__":
    app.run(debug=True)
