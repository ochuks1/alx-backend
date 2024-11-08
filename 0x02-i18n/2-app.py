#!/usr/bin/env python3
"""
Flask application with language locale support.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

# Configuration for Babel
class Config:
    """App configuration for Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """Selects the best match for the supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """Renders the main index page."""
    return render_template('2-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
