import os
import yagmail as yagmail
import functools

from werkzeug.utils import redirect
from flask import Flask, request, jsonify, g, url_for, session
from flask.templating import render_template
from forms import FormContactanos, FormRespuesta, FormLogin, FormRegistro
from models import mensaje, usuario

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.before_request
def cargar_usuario_autenticado():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = usuario.cargar(user_id)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):

        if g.user is None:
            return redirect( url_for('login'))

        return view(**kwargs)

    return

@app.route('/logout/')
@login_required
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/registro/", methods=["GET", "POST"])
def registro():
    if request.method == "GET":
        formulario = FormRegistro()
        return render_template('registro.html', form=formulario)
    else:
        formulario = FormRegistro(request.form)
        if formulario.validate_on_submit():
            obj_usuario = usuario(formulario.nombre.data, formulario.usuario.data, formulario.correo.data, formulario.password.data)
            if obj_usuario.insertar():
                return render_template('registro.html', exito="Se ha registrado su cuenta de usuario.")
        
        return render_template('registro.html',form=formulario, mensaje="Hay errores en su información por favor verifique.")

@app.route("/contactanos/", methods=["GET", "POST"])
@login_required
def contactanos():
    if request.method == "GET":
        formulario = FormContactanos()
        return render_template('contactanos.html', form = formulario)
    else:
        formulario = FormContactanos(request.form)
        if formulario.validate_on_submit():

            obj_mensaje = mensaje(p_id=0, p_nombre=formulario.nombre.data, p_correo=formulario.correo.data,
            p_mensaje=formulario.mensaje.data)

            if obj_mensaje.insertar():
                yag = yagmail.SMTP('alertasmisiontic2022@gmail.com','prueba123')
                yag.send(to=formulario.correo.data, subject="Su mensaje ha sido recibido",
                contents="Hola {0}, hemos recibido tu mensaje, pronto nos comunicaremos contigo.".format(formulario.nombre.data))
                return render_template('contactanos.html', form=FormContactanos(), mensaje="Su mensaje ha sido enviado.")

            else:
                return render_template('contactanos.html', form=FormContactanos(), errores="Contacte a soporte.")
     

        return render_template('contactanos.html', form=formulario, errores="Todos los datos son obligatorios.")

@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        formulario = FormLogin()
        return render_template("login.html", form=formulario)
    else:
        formulario = FormLogin(request.form)
        if formulario.validate_on_submit():
            obj_usuario = usuario('',formulario.username.data,'',formulario.password.data)

        if not obj_usuario.nombre.__contains__("'") and not obj_usuario.password.__contains__("'"):
            if obj_usuario.verificar():
                #Cuando se ha verificado el usuario, llenamos una variable de sesión
                #para utilizar posteriormente en el g.user y verificar si un usuario
                #se ha autenticado.
                session.clear()
                session['user_id'] = obj_usuario.usuario
                return redirect(url_for('get_listado_mensajes'))
        
        return render_template('login.html', mensaje="Usuario o contraseña no válido.")

@app.route('/mensajes/listado/json/', methods=["GET"])
def get_listado_mensajes_json():
    return jsonify(mensaje.listado())

@app.route('/mensajes/ver/json/<id>')
def get_mensaje_json(id):
    obj_mensaje =mensaje.cargar(id)
    if obj_mensaje:
        return obj_mensaje
    return jsonify({{"error":"No existe un mensaje con el id especificado"}})

@app.route('/mensajes/listado/')
def get_listado_mensajes():
    return render_template('listado_mensajes.html',lista=mensaje.listado())

@app.route('/mensajes/ver/<id>')
def get_mensaje(id):
    obj_mensaje =mensaje.cargar(id)
    if obj_mensaje:
        return render_template('ver_mensaje.html',item=obj_mensaje)
    return render_template('ver_mensaje.html',error="No existe el mensaje para el id especificado")

@app.route("/mensajes/respuesta/<id>",methods=["GET", "POST"])
def responder_mensaje(id):
    if request.method == "GET":
        formulario = FormRespuesta()
        obj_mensaje =mensaje.cargar(id)
        if obj_mensaje:
            formulario.nombre.data = obj_mensaje.nombre
            formulario.correo.data = obj_mensaje.correo
            formulario.mensaje_original.data = obj_mensaje.mensaje
            return render_template('responder_mensaje.html',id=id, form=formulario)

        return render_template('responder_mensaje.html',id=id, form=formulario, mensaje="No existe un mensaje para el id especificado")
    else:
        formulario = FormRespuesta(request.form)
        if formulario.validate_on_submit():

            obj_mensaje =mensaje.cargar(id)
            if obj_mensaje:
                obj_mensaje.respuesta = formulario.respuesta.data
                if obj_mensaje.responder():
                    yag = yagmail.SMTP('alertasmisiontic2022@gmail.com','prueba123')
                    yag.send(to=formulario.correo.data, subject="Su mensaje ha sido respondido.",
                    contents="Hola, la respuesta a tu mensaje es: {0}".format(formulario.respuesta.data))
            return render_template('responder_mensaje.html', id=id,form=FormRespuesta(), mensaje="La respuesta ha sido enviada.")

        return render_template('responder_mensaje.html', id=id,form=formulario, mensaje="Todos los campos son obligatorios.")
