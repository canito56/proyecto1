from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo, todo bien?"

# http://127.0.0.1:5000/params/Jorge Agustin Bardaro/63
@app.route("/params/")                      # Este se pone por si no ingresan ningun parametro
@app.route("/params/<name>/")
@app.route("/params/<name>/<int:edad>")
def params(name="No vino nombre", edad=0):   # Esto lo pone si no le paso parametros
    return "El parametro es: {} {}".format(name, edad)

if __name__ == "__main__":
    app.run(debug=True)                     # Esto es para que si cambio algo en el codigo se refleje en la web
