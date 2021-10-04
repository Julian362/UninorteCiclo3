import os
import yagmail as yagmail

from flask import Flask, request
from flask.templating import render_template
from forms import FormContactanos

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/contactanos/", methods=["GET", "POST"])
def contactanos():
    if request.method == "GET":
        formulario = FormContactanos()
        return render_template('contactanos.html', form = formulario)
    else:
        formulario = FormContactanos(request.form)
        if formulario.validate_on_submit():
            yag = yagmail.SMTP('alertasmisiontic2022@gmail.com','prueba123')
            yag.send(to=formulario.correo.data, subject="Su mensaje ha sido recibido",
            contents="Hola {0}, hemos recibido tu mensaje, pronto nos comunicaremos contigo.".format(formulario.nombre.data))
            return render_template('contactanos.html', form=FormContactanos(), errores="Su mensaje ha sido enviado.")

        return render_template('contactanos.html', form=formulario, errores="Todos los datos son obligatorios.")