from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@app.route('/promociones')
def promociones():
    return render_template('promociones.html')

app.run(host="localhost", port=4000, debug=True)