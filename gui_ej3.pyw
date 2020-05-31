import tkinter as tk
import modulos

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        root.title("GUI 3")
        root.geometry("650x350")
        self.hi_there = tk.Button(self)
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.create_widgets()

    def create_widgets(self):
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit.pack(side="bottom")

    @staticmethod
    def say_hi():                                   # No hay que ponerle self dentro de los parentesis
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

# ruta = modulos.get_path(prompt="ingresa una ruta: ")
# if ruta == r"c:\viejo":
#    raise ValueError("La ruta no puede ser ", ruta)