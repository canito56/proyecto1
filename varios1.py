# importar un modulo antes de usar una funcion que este en el mismo
import modulos

a = 1
b = 3
print(modulos.suma(a,b))

# encontrar posicion en un string (en info que seria = a 5) e imp lo que hay en esa
# posicion
var1 = "Hola viejo"
info = var1.find("viejo")
print(info)
print(var1[5:])

# para saber de que tipo es un dato
var2 = 15
print(var2, type(var2))
var3 = 1.5
print(var3, type(var3))
var4: complex = 3+5j
print(var4, type(var4))
var5 = "Hola viejo"
print(var5, type(var5))
var6 = 3 == 3
print(var6, type(var6))

# entrada de datos por teclado
ley1 = input("por favor, introduce un dato: ")
ley1 = ley1.lower()
while ley1 != "fin":
    print("string: ", ley1)
    ley1 = input("por favor, introduce un dato: ")
    ley1 = ley1.lower()

ley2 = int(input("introducir un numero entero: "))
while ley2 != 999:
    print("entero: ", ley2)
    ley2 = int(input("introducir un numero entero: "))

ley3 = float(input("introducir un numero flotante: "))
while ley3 != 999.0:
    print("flotante: ", round(ley3,2))  # esto redondea a 2 decimales
    ley3 = float(input("introducir un numero flotante: "))

ley4 = complex(input("introducir un numero complejo: "))
while ley4 != 0+0j:
    print("complejo: ", ley4)
    ley4 = complex(input("introducir un numero complejo: "))

# sentencia condicional if y while
ley5 = str(input("nombre alumno: "))
ley5 = ley5.lower()
calif = int(input("calificacion: "))
while ley5 != "fin":
    if calif > 3:
        print("Aprobado!")
    else:
        print("Burro!!!")
    ley5 = str(input("nombre alumno: "))
    ley5 = ley5.lower()
    if ley5 != "fin":
        calif = int(input("calificacion: "))
