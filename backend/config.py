# backend/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mi_clave_secreta')
    SQLALCHEMY_DATABASE_URI = 'postgresql://fact_user:tu_contraseña@localhost/facturacion'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
