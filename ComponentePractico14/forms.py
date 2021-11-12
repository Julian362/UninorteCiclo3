from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField, TextAreaField, PasswordField
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

class FormLogin(FlaskForm):
    username=StringField('Usuario',validators=[validators.required(), validators.length(max=50)])
    password=PasswordField('Contraseña', validators=[validators.required()])
    enviar=SubmitField('Iniciar sesión')

#Formulario de registro de usuarios
class FormRegistro(FlaskForm):
    usuario = StringField('Usuario', validators=[validators.required(), validators.length(max=50, min=5)])
    nombre = StringField('Nombre Completo', validators=[validators.required(), validators.length(max=100)])
    password = PasswordField('Contraseña', validators=[validators.required(), validators.length(max=20, min=8)])
    correo = StringField('Correo electrónico',validators=[validators.email(), validators.required(), validators.length(max=150)])
    enviar = SubmitField('Registrar')