# backend/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
