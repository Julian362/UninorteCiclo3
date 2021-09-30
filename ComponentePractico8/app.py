from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def registro():
    return render_template('formulario.html')