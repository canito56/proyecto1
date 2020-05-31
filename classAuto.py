class Coche:
    """ Abstraccion de los objetos coche """
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print("Tenemos", gasolina, "litros")

    def arrancar(self):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("No arranca")
        return self.gasolina

    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print("Quedan", self.gasolina, "litros")
        else:
            print("No se mueve")
        return self.gasolina

mi_coche = Coche(3)
print("Si claro, tenemos", mi_coche.gasolina, "litros")
print(mi_coche.arrancar())

while mi_coche.conducir() > 0:
    print(mi_coche.conducir())

print(mi_coche.arrancar())
print(mi_coche.conducir())

print(mi_coche.__str__())       # Imprime el obj como un string
