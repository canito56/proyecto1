import modulos
print("*** Programa que indica si un nro es par o impar *** \n")
nro = int(input("Introduzca un numero: "))
while nro > 0:
    if nro % 2 == 0:
        print("El nro ", nro, "es par")
    else:
        print("El nro ", nro, "es impar")
    nro = int(input("Introduzca un numero: "))

# llama a get_path
print("\n Introduzca una ruta: \n")
prompt = ""
print(modulos.get_path(prompt))

# llama a genera_pares
limite = int(input("\n Introduzca un limmite: "))
while limite > 0:
    print("\n", modulos.genera_pares(limite))
    limite = int(input("\n Introduzca un limmite: "))

# llama a genera_pares_generador
limite = int(input("\n Introduzca un limmite: "))
while limite > 0:
    misPares = modulos.genera_pares_generador(limite)
    for i in misPares:
        print(i)
    limite = int(input("\n Introduzca otro limmite: "))

# devolucion uno a uno
limite = int(input("\n Introduzca el ultimo limmite: "))
misPares = modulos.genera_pares_generador(limite)
print(next(misPares))
