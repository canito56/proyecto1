print("\n *** Recorre archivo con sentencia while \n")
f = open("nombres", "r")
linea = f.readline()
while linea != "":
    print(linea)
    linea = f.readline()
f.close()

# lee con for
print("\n *** Recorre archivo con sentencia for \n")
f = open("nombres", "r")
for linea in f:
    print(linea)
f.close()

f = open("nombres", "r")
print("\n El archivo en forma horizontal: ", f.readlines())
f.close()
f = open("nombres", "r")
print("\n El archivo tiene ", len(f.readlines()), " lineas \n")
f.close()

f = open("nombres", "r")
f.fileno()
f.close()