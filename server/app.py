from flask import Flask
from .config import Config
from server.models import Appearance,Guest,User,Episode,db
from flask_migrate import Migrate

#Create a Flask app instance
app=Flask(__name__)
app.config.from_object(Config)
#Binds app to db Object
db.init_app(app)
# Create and bind the migrate object to app and db
migrate = Migrate(app, db)


