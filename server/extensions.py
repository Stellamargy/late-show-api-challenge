from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
bcrypt=Bcrypt()
migrate =Migrate()
db =SQLAlchemy()
fake=Faker()  