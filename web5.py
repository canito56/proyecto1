import pymysql
from flask import Flask
from flask import render_template

db = pymysql.connect(host="localhost",
                     user="root",
                     password="",
                     db="empleados")

app = Flask(__name__, template_folder="templates")
my_list = []

@app.route("/empleadosKN")
def index():
    cursor = db.cursor()
    sql = "select * from empleado"
    cursor.execute(sql)
    filas = cursor.fetchall()
    for row in filas:
        legajo  = row[0]
        docid   = row[1]
        nombre  = row[2]
        fecini  = row[3]
        direc   = row[4]
        edad    = row[5]
        cargo   = row[6]
        nacion  = row[7]
        fecbaja = row[8]
        linea   = legajo + " " + str(docid) + " " + nombre + " " + str(fecini) + " " + direc + " " + \
                str(edad) + " " + cargo + " " + nacion + " " + str(fecbaja)
        my_list.append(linea)
    return render_template("html_web5.html", list=my_list)

if __name__ == "__main__":
    app.run(debug=True)
