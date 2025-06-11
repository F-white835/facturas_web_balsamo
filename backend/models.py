from extensions import db

class Factura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    tipo_comprobante = db.Column(db.String(50), nullable=False)
    forma_pago = db.Column(db.String(50), nullable=False)
    nit = db.Column(db.String(50), nullable=True)

