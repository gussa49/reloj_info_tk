

import tkinter as tk
from PIL import Image, ImageTk
from time import strftime


ventana = tk.Tk()
ventana.title("Reloj Digital y Nombres de Grupo")
ventana.geometry("500x1000")
ventana.resizable(False, False)

imagen = Image.open("img.reloj1.jpeg")  
imagen = imagen.resize((500, 500))
imagen_fondo = ImageTk.PhotoImage(imagen)


etiqueta_imagen = tk.Label(ventana, image=imagen_fondo)
etiqueta_imagen.pack()


def actualizar_tiempo():
    hora_actual = strftime("%I:%M:%S %p")
    dia_actual = strftime("%A")  
    fecha_actual = strftime("%d de %B de %Y") 
    etiqueta_hora.config(text=hora_actual)
    etiqueta_dia.config(text=dia_actual)
    etiqueta_fecha.config(text=fecha_actual)
    ventana.after(1000, actualizar_tiempo)


etiqueta_hora = tk.Label(ventana, font=("Arial", 38, 'bold'), fg="orange", bg="dark slate blue")
etiqueta_hora.pack()


etiqueta_dia = tk.Label(ventana, font=("Arial", 38), fg="white", bg="dark slate blue")
etiqueta_dia.pack()

etiqueta_fecha = tk.Label(ventana, font=("Arial", 28), fg="white", bg="dark slate blue")
etiqueta_fecha.pack()


nombres_integrantes = "GRUPO 10\n *Tourn Braian\n *Dominguez Alexis\n *Borda Nestor Alejandro\n *García Alberto Gustavo\n *Alex Oliva\n *García María Amalia\n "
etiqueta_nombres = tk.Label(ventana, text=nombres_integrantes, font=("Arial", 20), bg="RED", fg="white")
etiqueta_nombres.pack()

actualizar_tiempo()


ventana.mainloop()