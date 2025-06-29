from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
bcrypt=Bcrypt()
migrate =Migrate()
db =SQLAlchemy()    