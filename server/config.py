from dotenv import load_dotenv
import os
# load environmental variables from .env
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=False