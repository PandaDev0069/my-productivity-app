import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://productivity_app_e4h6_user:2j2EjIP64t5npmKVU2WoVs8V01CxXybA@dpg-cujkvlogph6c73bhsamg-a.singapore-postgres.render.com/productivity_app_e4h6')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwtsecret')
