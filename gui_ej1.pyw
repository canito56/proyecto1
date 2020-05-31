import tkinter as tk

miventana = tk.Tk()
miventana.title("Primera ventana")
miventana.geometry("600x400")
miventana.config(background="#2798FA")
main_title = tk.Label(text="TKINTER GUI - Jorge", font=("Tahoma", 14), bg="#ff7763", fg="black", width="60", height="4")
main_title.place(x=0, y=50)
miventana.mainloop()            # La ventana nececita estar en un bucle infinito

# Si ejecutamos desde el archivo .py, nos abre atras la ventana de comandos. Si redefinimos el pgm como .pyw la
# abre sola (la w es de windows).
