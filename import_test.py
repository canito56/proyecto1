import sys

mensaje = ""
try:
    import caca
except ImportError:
    mensaje = "nene, caca no existe!"
finally:
    raise ValueError(mensaje)

w_path = sys.path
print(w_path)
# El resultado es:
# ['C:\\Users\\Jorge\\PycharmProjects\\proyecto1',
# 'C:\\Users\\Jorge\\PycharmProjects\\proyecto1',
# 'C:\\Users\\Jorge\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip',
# 'C:\\Users\\Jorge\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs',
# 'C:\\Users\\Jorge\\AppData\\Local\\Programs\\Python\\Python38-32\\lib',
# 'C:\\Users\\Jorge\\AppData\\Local\\Programs\\Python\\Python38-32',
# 'C:\\Users\\Jorge\\PycharmProjects\\proyecto1\\venv',
# 'C:\\Users\\Jorge\\PycharmProjects\\proyecto1\\venv\\lib\\site-packages']
# Siempre que se haga un import, python va a buscar en estos directorios en ese orden, esto depende de mi sist operativo
# y de como tenga yo instaladas las cosas.
# Se puede agregar un nuevo camino a sys.path en tiempo de ejecucion, asi la busqueda de algun modulo tambien se
# hara en ese dir. Obviamente si se para la ejecucion, el camino agregado desaparece.