from tkinter import *

raiz = Tk()
raiz.title("Primera ventana de pruebas")
# raiz.resizable(0, 0)  # No se puede redimensionar la ventana. Si pongo (1, 0) se puede a lo ancho y (0, 1) a lo alto
# raiz.iconbitmap("c:/users/carpeta/gato.ico")  # Las imagenes deben ser .ico, en google puedo poner convert .ico
raiz.geometry("850x450")  # Esto se puede sacar porque la raiz se va a adaptar al tamaño del Frame
raiz.config(bg="blue", bd=45, relief="groove", cursor="hand2")
mi_frame = Frame()  # Construyo un Frame
mi_frame.pack()  # Mete el frame dentro de raiz
# mi_frame.pack(side="right", anchor="w") # Mete el Frame dentro de la raiz y lo pone donde quiero (a la der y west)
# mi_frame.pack(fill="y", expand="True")  # Se expande verticalmente (todo esto se puede ver en la doc del link)
# mi_frame.pack(fill="x", expand="True")  # Se expande horizontalmente
mi_frame.config(bg="red", width="650", height="350")  # Le cambio el color de fondo y las dimensiones
mi_frame.config(bd=35)  # Cambia tamaño del borde
mi_frame.config(relief="sunken")  # Cambia relieve del frame
mi_frame.config(cursor="pirate")  # Cambia el cursor dentro del frame
raiz.mainloop()  # La ventana necesita estar en bucle infinito
