from server import app
from flask import Blueprint

user_bp=Blueprint('user',__name__,url_prefix='/users')


