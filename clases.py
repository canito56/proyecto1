class Fib:
    """ iterador que genera los nu´meros de la secuencia de Fibonacci """
    def __init__(self, maximo):
        self.maximo = maximo

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.maximo:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib
