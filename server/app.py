from flask import Flask
from .config import Config
#Create a Flask app instance
app=Flask(__name__)
app.config.from_object(Config)

