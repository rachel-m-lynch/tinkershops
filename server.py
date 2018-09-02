from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, session
from flask import jsonify
from flask_debugtoolbar import DebugToolbarExtension

import os

app = Flask(__name__)

app.secret_key = "a much better secret key to come"

app.jinja_env.undefined = StrictUndefined

###############################################################################


@app.route('/')
def index():
    """Homepage"""

    return render_template('index.html')

@app.route('/projects')
def show_projects():
    """Projects page"""

    return render_template('projects.html')

@app.route('/login')
def show_login():
    """Show login page"""

    return render_template('login.html')

@app.route('/add_projects')
def add_projects():
    """Add a project"""

    return render_template('add-projects.html')

###############################################################################


if __name__ == "__main__":
    app.debug = True
    # connect_to_db(app)
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
