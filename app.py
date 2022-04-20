import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db, render_as_batch=True)

class Login(db.Model):
    __tablename__ = "Login"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    is_logged_in = db.Column(db.Boolean())
    # where_logged_in = db.Column(db.String(120), nullable=True)
    what_he_is_doing = db.Column(db.String(200), nullable=True)


    def __init__(self, username, is_logged_in, what_he_is_doing):
        self.username = username
        self.is_logged_in = is_logged_in
        # self.where_logged_in = where_logged_in
        self.what_he_is_doing = what_he_is_doing

    def __repr__(self):
        return f'{self.username} - logged in {self.is_logged_in}, doing {self.what_he_is_doing}'