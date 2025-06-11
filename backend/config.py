# backend/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mi_clave_secreta')  # Puedes cambiar esta clave si quieres
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')       # Esta línea es clave para Render
    SQLALCHEMY_TRACK_MODIFICATIONS = False
