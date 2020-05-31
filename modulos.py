def saludo():
    print('Hola viejo!')


def suma(x, y):
    return x + y


def get_path(prompt):
    path = input(prompt)
    return path


def genera_pares(limite):
    num = 1
    lista = []
    while num <= limite:
        lista.append(num * 2)
        num = num + 1
    return lista


def genera_pares_generador(limite):
    num = 1
    while num <= limite:
        yield num * 2
        num = num + 1
