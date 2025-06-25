from .database import db
class User(db.Model):
    #table name
    __tablename__ = 'users'
    #columns with their respective datatypes and constraints
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password= db.Column(db.String(255), nullable=False)
