import yagmail as yagmail
from flask import Flask, render_template, request
from utils import *
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
@app.route('/login/', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/registro/', methods=['GET','POST'])
def registro():
    if request.method == 'GET':
        return render_template('formulario.html')
    else:
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        sexo = request.form['sexo']
        email = request.form['email']
        password = request.form['password']
        declaracion = request.form['declaracion']

    errores = ""
    exito = ""

    if len(nombre) <=0:
        errores+="Debe escribir un nombre válido"

    if len(apellidos) <=0:
        errores+="Debe escribir un apellido"

    if not isEmailValid(email):
        errores+= "Debe digitar un Email valido"

    if not isPasswordValid(password):
        errores+= "Debe digitar una contraseña valida"

    if not declaracion == "S":
        errores+= "Debe aceptar los terminos y condiciones"

    if not errores:
        exito = "Su cuenta ha sido registrada"
        yag = yagmail.SMTP('alertasmisiontic2022@gmail.com','prueba123')
        yag.send(to=email, subject="Activación de cuenta vacunación covid 19")
        contents= "bienvenido {0}, usa este link para activar tu cuenta.".format(nombre +' '+ apellidos)
        return render_template('login.html', exito=exito)
    else :
        return render_template('formulario.html', errores=errores)
