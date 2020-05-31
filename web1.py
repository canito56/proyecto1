from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo, todo bien?"

@app.route("/saluda")
def saluda():
    return "Saludos desde aqui"

# http://127.0.0.1:5000/params?par1=Jorge_Bardaro
# Se podria sequir enviendo parametros asi: http://127.0.0.1:5000/params?params1=Jorge_Bardaro&params2=Ing_Sistemas
@app.route("/params")
def params():
    par1 = request.args.get("params1", "no contiene par1")
    par2 = request.args.get("params2", "no contiene par2")
    return "El parametro es: {},{}".format(par1, par2)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
