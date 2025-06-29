from flask import Flask
from .config import Config
from server.models import Appearance,Guest,User,Episode,db
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from server.controllers import user_bp,auth_bp
from .extensions import bcrypt

#Create a Flask app instance
app=Flask(__name__)
app.config.from_object(Config)
#Binds app to db Object
db.init_app(app)
# Create and bind the migrate object to app and db
migrate = Migrate(app, db)
#Bind app to bcrypt
bcrypt.init_app(app)


#Register user blueprint
app.register_blueprint(user_bp)
#Register auth blueprint
app.register_blueprint(auth_bp)


