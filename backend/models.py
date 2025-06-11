from extensions import db
from models import Factura

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    tipo_comprobante = db.Column(db.String(50))
    forma_pago = db.Column(db.String(50))
    nit = db.Column(db.String(20))

