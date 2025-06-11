# backend/app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateTimeField
from wtforms.validators import DataRequired
from models import db, Factura
from datetime import datetime

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
with app.app_context():
    db.create_all()  # <- crea las tablas si no existen

class FacturaForm(FlaskForm):
    cliente = StringField('Cliente', validators=[DataRequired()])
    monto = FloatField('Monto', validators=[DataRequired()])
    fecha = DateTimeField('Fecha', default=datetime.utcnow, validators=[DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FacturaForm()
    if form.validate_on_submit():
        factura = Factura(
            cliente=form.cliente.data,
            monto=form.monto.data,
            fecha=form.fecha.data
        )
        db.session.add(factura)
        db.session.commit()
        return redirect(url_for('index'))
    facturas = Factura.query.all()
    return render_template('index.html', form=form, facturas=facturas)

if __name__ == '__main__':
    app.run(debug=True)
