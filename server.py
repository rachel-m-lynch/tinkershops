from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask import jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import User, UserProject, Project
from model import connect_to_db, db

import os

app = Flask(__name__)

app.secret_key = "a much better secret key to come"

app.jinja_env.undefined = StrictUndefined

###############################################################################


@app.route('/')
def index():
    """Homepage"""

    return render_template('index.html')


@app.route('/login')
def show_login():
    """Show login page"""

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def complete_login():
    """Show login page"""

    username = request.form.get('username')
    password = request.form.get('password')
    
    user = User.query.filter_by(username=username).first()

    if not user or user.password != password:
        flash('Invalid password')
        return redirect('/login')

    session['user_id'] = user_id

    flash("Logged In")

    return redirect(f'/users/{user.id}')


@app.route('/add_projects')
def display_add_form():
    """Display the add project form"""

    return render_template('add-projects.html')


@app.route('/add_projects', methods=['POST'])
def add_projects():
    """Add a project to the database"""

    first_name = request.form.get('first_name')

    p_name = request.form.get('p_name')

    p_type = request.form.get('p_type')

    p_summary = request.form.get('p_summary')

    p_picture = request.form.get('p_picture')

    p_description = request.form.get('p_description')

    contributor = User.query.get(first_name)

    print(contributor)

    user_id = contributor.id

    print(user_id)

    project = Project.query.filter_by(p_name=p_name).first()

    if project:
        flash('Project name is taken')
        return redirect('/add_projects')

    new_project = Project(p_name=p_name,
                          p_type=p_type,
                          p_summary=p_summary,
                          p_picture=p_picture,
                          p_description=p_description,
                          user_id=user_id)

    db.session.add(new_project)
    db.session.commit()

    flash('New Project Added')

    return redirect('/')



@app.route('/h_projects')
def hardware_projects():
    """Display hardware projects"""

    return render_template('hardware-projects.html')


@app.route('/s_projects')
def software_projects():
    """Display software projects"""

    return render_template('software-projects.html')


@app.route('/c_projects')
def combination_projects():
    """Display combination projects"""

    return render_template('combination-projects.html')


@app.route('/contact')
def display_contact():
    """Display contact page"""

    return render_template('contact.html')


###############################################################################


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
