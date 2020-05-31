from tkinter import *

def colocar_nombre(self):
    varnombre.set("Jorge Agustin")

root = Tk()
root.title("JBPY001 - INGRESO DE DATOS")
# root.resizable(0, 0)
mi_frame = Frame(root, width=1200, height=550)
mi_frame.pack()
# titulo = Label(mi_frame, text="Hola programadores Python", fg="red", font=("Comic sans MS", 18)).grid(row=0,
# column=150)
varnombre = StringVar()
Label(mi_frame, text="Nombre ").grid(row=0, column=0, sticky="W", pady=10)
nombre = Entry(mi_frame, textvariable=varnombre, width=20).grid(row=0, column=1, sticky="W", pady=10)

Label(mi_frame, text="Apellido ").grid(row=0, column=2, sticky="W", pady=10)
apellido = Entry(mi_frame, width=20).grid(row=0, column=3, sticky="w"
                                                                  "E", padx=10, pady=10)

Label(mi_frame, text="Direccion ").grid(row=1, column=0, sticky="W", pady=10)
direccion = Entry(mi_frame, width=20).grid(row=1, column=1, sticky="W", pady=10)

Label(mi_frame, text="Contraseña ").grid(row=2, column=0, sticky="W", pady=10)
password = Entry(mi_frame)
password.grid(row=2, column=1, sticky="W", pady=10)
password.config(show="*")

Label(mi_frame, text="Comentarios").grid(row=3, column=0, sticky="W", pady=10)
coment = Text(mi_frame, width=40, height=5)
coment.grid(row=3, column=1, sticky="W", pady=10)

scrollvert = Scrollbar(mi_frame, command=coment.yview)
scrollvert.grid(row=3, column=2, sticky="nsew")
coment.config(yscrollcommand=scrollvert.set)

Button(mi_frame, text="Quit", command=mi_frame.quit).grid(row=300, column=2, sticky="W", pady=10)
b_show = Button(mi_frame, text="Show")
b_show.grid(row=300, column=1, sticky="W", pady=10)
b_show.bind("<Button-1>", colocar_nombre)

root.mainloop()

# mi_photo = PhotoImage(mi_frame, file="python1.png")  # o imagen.png"
# Label(root, image=mi_photo).place(x=50, y=100)
