from flask import Flask
from .config import Config
from server.models import Appearance,Guest,User,Episode
from flask_bcrypt import Bcrypt
from server.controllers import user_bp,auth_bp
from .extensions import bcrypt,migrate,db

#Create a Flask app instance
app=Flask(__name__)
app.config.from_object(Config)
#Binds app to db Object
db.init_app(app)
#  bind the migrate object to app and db
migrate.init_app(db=db,app=app)
#Bind app to bcrypt
bcrypt.init_app(app)


#Register user blueprint
app.register_blueprint(user_bp)
#Register auth blueprint
app.register_blueprint(auth_bp)


