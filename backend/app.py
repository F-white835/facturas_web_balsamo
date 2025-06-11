from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateTimeField, SubmitField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime

from backend.extensions import db
from backend.models import Factura

app = Flask(__name__)
app.config.from_object('backend.config.Config')
db.init_app(app)

with app.app_context():
    db.create_all()

class FacturaForm(FlaskForm):
    cliente = StringField('Cliente', validators=[DataRequired()])
    monto = FloatField('Monto', validators=[DataRequired()])
    fecha = DateTimeField('Fecha', validators=[DataRequired()])
    tipo_comprobante = SelectField('Tipo de Comprobante', choices=[
        ('Factura', 'Factura'),
        ('Recibo', 'Recibo'),
        ('Ticket', 'Ticket')
    ])
    forma_pago = SelectField('Forma de Pago', choices=[
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia', 'Transferencia')
    ])
    nit = StringField('NIT')
    submit = SubmitField('Generar')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FacturaForm()
    if form.validate_on_submit():
        factura = Factura(
            cliente=form.cliente.data,
            monto=form.monto.data,
            fecha=form.fecha.data,
            tipo_comprobante=form.tipo_comprobante.data,
            forma_pago=form.forma_pago.data,
            nit=form.nit.data
        )
        db.session.add(factura)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=form)
