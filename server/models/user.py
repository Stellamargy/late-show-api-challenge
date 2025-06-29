from .database import db
# from server.utilis import password
from server.extensions import bcrypt


class User(db.Model):
    #table name
    __tablename__ = 'users'
    #columns with their respective datatypes and constraints
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    _password= db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User id={self.id} username='{self.username}'>"


    @property
    def password(self):
        raise AttributeError('password is private attribute')
        

    @password.setter
    def password(self, password):
        self._password =bcrypt.generate_password_hash(password).decode('utf-8') 
    # Returns boolean - compares input password and password hash in db 
    def verify_password(self, password):
        return bcrypt.check_password_hash(self._password, password)
