"""Models and database functions for the Tinkershops website"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

###############################################################################
# Model definitions 


class User(db.Model):
    """Save the user's information"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String, nullable=False)

    last_name = db.Column(db.String, nullable=False)

    email = db.Column(db.String, unique=True, nullable=False)

    password = db.Column(db.String, nullable=False)

    administrator = db.Column(db.String, nullable=False, default=False)

    projects = db.relationship('Project', secondary='user_projects', backref='users')

    def __repr__(self):
        """Display user's information"""

        return f"""<User ID: {self.id}
                   Username: {self.username}
                   Email: {self.email}
                   Password: {self.password}
                   Administrator: {self.administrator}>"""


class UserProject(db.Model):
    """Join the user and the projects"""

    __tablename__ = "user_projects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    projects_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    def __repr__(self):
        """Display information about the user's projects"""

        return f"""<User-Projects ID: {self.id}
                   User ID: {self.users_id}
                   Project ID: {self.projects_id}>"""


class Project(db.Model):
    """Projects displayed on the Tinkershops website"""

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    p_name = db.Column(db.String, nullable=False)

    p_summary = db.Column(db.String, nullable=False)

    p_picture = db.Column(db.String)

    p_description = db.Column(db.String)

    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        """Display information about the project"""

        return f"""<Project ID: {self.id}
                   Project Name: {self.p_name}
                   Project Summary: {self.p_summary}
                   Project Picture: {self.p_picture}
                   Project Description: {self.p_description}>"""


###############################################################################

def connect_to_db(app, database='postgresql:///tinkershops'):
    """Connect the database to the Flask app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")
    db.create_all()