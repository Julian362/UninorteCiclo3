from flask import Flask, render_template
app = Flask(__name__,template_folder='static/templates')
@app.route('/')

@app.route('/registro')
def registro():
    return render_template('formulario.html')