import pymysql
db = pymysql.connect(host="localhost",
                     user="root",
                     password="",
                     db="empleados")
try:
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
        cargo   = row[5]
        nacion  = row[6]
        fecbaja = row[7]
        print(legajo, docid, nombre, fecini, direc, cargo, nacion, fecbaja)
except:
    print("Error: No se pudo acceder a la base de datos")
finally:
    db.close()
