import clases

#for n in clases.Fib(200):
#    print(n, end=" ")

f = clases.Fib(300)

for n in f.__iter__():
    print(n, end=" ")
