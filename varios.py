import os
import fractions
import sys
import re

print(sys.modules["fractions"])     # Muestra la ruta del modulo fractions.py

# Cadenas
print("\n--- Cadenas")
s = "100 BROAD ROAD APT. 3"
s2 = re.sub(r"\bROAD\b", "RD.", s)
print("La cadena: ", s, "  se reemplaza por la cadena: ", s2)

# Tipos
print("\n--- Tipos")
lista = [1, 2, 3, 4, 5]
print(type(lista))
print(type(3+4j))
print(type(2.0))
print(type(2))
print(type(1 + 2.1))
c = 3+5j
print(c, isinstance(c, complex))        # Pregunta si es un complejo e imprime la respuesta (True/False)

# Fracciones
print("\n--- Fracciones")
f = fractions
a = f.Fraction(2, 3)
b = f.Fraction(2, 3)
c = a + b
print("c = ", c)

# Los nros se pueden usar como valores booleanos. El cero es falso, cualquier otro valor es verdadero
print("\n--- Nros como valores booleanos ")
def es_true(linea, algo):
    if algo:
        print(linea, ": valor = ", algo, ",", " si, es true")
    else:
        print(linea, ": valor = ", algo, ",", " no, es false")
es_true("1", 1)
es_true("2", -1)
es_true("3", 0)
es_true("4", f.Fraction(1, 2))
es_true("5", f.Fraction(0, 2))

# Listas
print("\n--- Listas")
lista = [1, 2, "a", "b", 3, 3 + 5j, "cualquier texto", es_true("6", 0)]
print(lista)
print(lista[-3])    # Tercer valor contando desde el final
print(lista[-1])    # Ultimo elemento de la lista
print(lista[1:3])
print(lista[1:-1])
print(lista[0:3])
print(lista[:3])
print(lista[3:])
print(lista[:])
lista = lista + ["vos", 69]
print(lista)
lista.append(True)
print(lista)
lista.extend(["uno", "dos"])
print(lista)
lista.insert(0, "dos")                  # Inserta "dos" en la primera posicion, o sea 0
print(lista)
lista.append(["yo", "tu", "el"])        # Inserta una nueva lista dentro de lista
print(lista)
print(lista.count("dos"))               # Cuenta cuantas veces esta "dos" en la lista
print("dos" in lista)                   # Imprime True si "dos" esta en la lista
print("caca" in lista)                  # Imprime False
print(lista.index(None))                # Muestra en que posicion esta None
print(lista.index("dos"))               # Imprime 0 porque esta mas de una vez
print(lista.index(["yo", "tu", "el"]))  # Imprime la posicion en que se encuentra la lista insertada dentro de lista
del lista[1]                            # Elimina elemento 1, despues de eliminar o remover un elem, todos los demas
                                        # se corren para rellenar el espacio
print(lista)
lista.remove(None)                      # Remueve el elemento None
print(lista)
lista.pop()                             # Elimina y devuelve el ultimo elemento
print(lista)
lista.pop(1)                            # Elimina el elemento 1, todos los demas se corren. Si eliminas con pop() y no
                                        # hay elem en la lista, se devuelve un error "IndexError : pop from empty list"
print(lista)
lista2 = [3, 9, 1, 7, 6, 5, 4, 2, 8]
print(lista2)
lista2.sort()                           # En esta linea no permite hacer todo junto (sort y print)
print(lista2)
# print(lista.index("traba"))           # Da el error: ValueError : list.index("traba"): "traba" not in list

# Listas por Comprension
print("\n--- Listas por Comprension")
lista = [1, 2, 3, 4]
print([elem * 2 for elem in lista])     # El resultado es: [2, 4, 6, 8]
print(lista)                            # lista no cambia
lista = [elem * 2 for elem in lista]
print(lista)                            # Ahora si cambia

# Tuplas
print("\n--- Tuplas")
print("Las tuplas se definen igual que las listas (pero con parentesis) y tienen el mismo tratamiento, \n"
      "con la diferencia de que no se pueden modificar con una operacion, se pueden volver a definir asignando los \n"
      "valores nuevos. Las tuplas son mas rapidas que las listas.")
tupla = 1                               # Si la tupla tiene un solo elemento, se define sin parentesis
print(tupla)
tupla = (1, 2, 3, 4, 5)
print(tupla)
(lunes, martes, miercoles, jueves, viernes, sabado, domingo) = range(7)
print(miercoles)                        # Resultado = 2
print(viernes)                          # Resultado = 4
a = sabado
print(a)                                # Resultado = 5

# Conjuntos
print("\n--- Conjuntos")                # Con dos conjuntos se pueden realizar todas las op tipicas sobre ellos.
                                        # Los conjuntos son clases
conj1 = {1, "a", "hola", 2, 3}
print(conj1)
lista2 = [7, 5, 6, 11, 8]
conj2 = set(lista2)
print(conj2)
print(len(conj2))
conj2.add(9)                            # Si se agrega un valor que ya existe, no hace nada
print(conj2)
conj2.update(conj1)                     # Agrega a conj2 todos los valores de conj1
print(conj2)
conj2.discard("hola")                   # Elimina un elemento. Si el elemento no existe, no pasa nada.
print(conj2)
conj2.remove("a")                       # Elimina un elemento. Si el elemento no existe, da error "KeyError: x"
print(conj2)
conj3 = {"a", "b", "c"}
print(conj3)
conj3.clear()                           # Queda el conjunto vacio, similar a crearlo asi: conj3 = set()
print(conj3)                            # Si se intenta extraer un valor de un conjunto vacio, da KeyError
print(12 in conj2)                      # Imprime False
print(3 in conj2)                       # Imprime True
print("conj1 = ", conj1)
print("conj2 = ", conj2)
print("union = ", conj1.union(conj2))   # Imprime union entre conj1 y conj2
print("inter = ", conj1.intersection(conj2))   # Imprime interseccion entre conj1 y conj2
print("dif = ", conj1.difference(conj2))       # Imprime diferencia entre conj1 y conj2
print("difSim = ", conj1.symmetric_difference(conj2))   # Imprime diferencia simetrica (saca valores q estan en los dos)
print(conj1.issubset(conj2))             # Pregunta si el conj1 esta incluido en el conj2, en este caso es False
print(conj1.issuperset(conj2))           # Pregunta si el conj2 incluye al conj1, en este caso es False

# Diccionarios
print("\n--- Diccionarios")              # Son un conjunto desordenado de parejas clave-valor
dic1 = {"Jorge": "Ciel", "lenguaje": "python"}
print(dic1)
print(dic1["Jorge"], dic1["lenguaje"])   # Esto imprime "Ciel python"
# print(dic1["python"])                  # Esto da KeyError
dic2 = {1: 111, 2: 222}
print(dic2)
dic2[2] = 333                            # Esto modifica el valor de la clave 2
print(dic2)
dic2[3] = 444                            # Esto agrega 3: 444
print(dic2)
print(dic1.get("Chiche", "No encontro"))  # Imprime el valor de Chiche, si no lo encuentra imprime No encontro
print(dic1.keys())                        # Imprime las claves del diccionario
print(dic1.items())                       # Imprime una lista de tuplas con pares clave-valor
print(dic1.values())                      # Imprime lista de valores del diccionario

# Muestra al margen para ver como se puede insertar algo en un string:
# >>> a = 1
# >>> b = 2
# >>> c = 3
# >>> "Aqui pone a {0}, aqui pone b {1}, aqui pone c {2}".format(a, b, c)
# 'Aqui pone a 1, aqui pone b 2, aqui pone c 3'

# Dir de trabajo actual
print("\n--- Dir de trabajo actual")
print(os.getcwd())                       # Esto muestra: C:\Users\Jorge\PycharmProjects\proyecto1
os.chdir("C:/Users/Jorge/PycharmProjects/proyecto1/templates")  # Conviene poner las barras / que son universales
print(os.getcwd())                       # Esto muestra: C:\Users\Jorge\PycharmProjects\proyecto1\templates


# Mensajes de Error
lista = [2, 4, 9, 3, 7, 5]
mensaje = ""
try:
    print(lista.sort(key=_T))
except NameError:
    mensaje = "No existe _T, bobo!!"
finally:
    raise NameError(mensaje)
