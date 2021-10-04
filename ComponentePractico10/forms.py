from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField, TextAreaField
from wtforms import validators

class FormContactanos(FlaskForm):
    nombre = StringField('Nombre',validators=[validators.required(), validators.length(max=100)])
    correo = StringField('Correo Electrónico',validators=[validators.required(), validators.length(max=150)])
    mensaje = TextAreaField('Mensaje', validators=[validators.required(), validators.length(max=500)])
    enviar = SubmitField('Enviar Mensaje')