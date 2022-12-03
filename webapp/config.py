import os
from dotenv import load_dotenv

class Config:
    load_dotenv('main/.env')
    SECRET_KEY = os.getenv('REMEMBER_ME')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'