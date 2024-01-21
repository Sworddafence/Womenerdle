# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SuperVar(db.Model):
    #__tablename__ = 'super_var'  # Specify the table name explicitly
    index = db.Column(db.Integer, primary_key=True)

class User(db.Model):
   # __tablename__ = 'user'  # Specify the table name explicitly
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    hint1 = db.Column(db.String(120), unique=False, nullable=False)
    hint2 = db.Column(db.String(120), unique=False, nullable=False)
    hint3 = db.Column(db.String(120), unique=False, nullable=False)
    hint4 = db.Column(db.String(120), unique=False, nullable=False)
    hint5 = db.Column(db.String(120), unique=False, nullable=False)


