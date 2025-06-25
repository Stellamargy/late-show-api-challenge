from dotenv import load_dotenv
import os
# load environmental variables from .env
load_dotenv()

class Config:
    
    FLASK_APP=os.getenv('FLASK_APP')
    FLASK_DEBUG=bool(os.getenv('FLASK_DEBUG'))