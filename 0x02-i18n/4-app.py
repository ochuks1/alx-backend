#!/usr/bin/env python3
"""
Flask app with URL parameter-based locale selection.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

class Config:
    """App configuration for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """Determines the best match with supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """Renders the main index page."""
    return render_template('4-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
