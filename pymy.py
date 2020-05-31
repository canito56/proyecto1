import pymysql
db = pymysql.connect(host="localhost",
                     user="root",
                     password="",
                     db="empleados")
cursor = db.cursor()
cursor.execute("select version()")
version = cursor.fetchone()
print(version)
