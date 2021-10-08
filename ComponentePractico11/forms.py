from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField, TextAreaField
from wtforms import validators
from wtforms.widgets.core import SubmitInput, TextArea

class FormContactanos(FlaskForm):
    nombre = StringField('Nombre',validators=[validators.required(), validators.length(max=100)])
    correo = StringField('Correo Electrónico',validators=[validators.required(), validators.length(max=150)])
    mensaje = TextAreaField('Mensaje', validators=[validators.required(), validators.length(max=500)])
    enviar = SubmitField('Enviar Mensaje')

class FormRespuesta(FlaskForm):
    nombre = StringField('Nombre')
    correo = StringField('Correo Electrónico', validators=[validators.required()])
    mensaje_original = TextAreaField('Mensaje Original')
    respuesta = TextAreaField('Respuesta', validators=[validators.required(message="La respuesta es obligatoria")])
    enviar = SubmitField("Enviar Respuesta")

