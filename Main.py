#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
from Tkinter import *
import tkMessageBox
from threading import Thread
import getpass

ventana = Tk()
ventana.title("Youtube-dl")
ventana.geometry("600x100")
ventana.resizable(width=False, height=False)

def comenzarDescarga():
    if(url.get() == ""):
        tkMessageBox.showinfo("Mensaje", "Ingresa una url")
    else:
        labelLoad.grid()
        botonDescargar.config(state="disabled")
        try:
            subprocess.check_call(["youtube-dl", "-x", "--audio-format", "mp3", url.get()], cwd = "/home/" + getpass.getuser() + "/Escritorio/")
            url.delete(0,END)
            labelLoad.grid_remove()
            botonDescargar.config(state="normal")
            tkMessageBox.showinfo("Mensaje", "Listo, la canción se ha descargado!")
        except subprocess.CalledProcessError as e:
            tkMessageBox.showinfo("Error a descargar la canción", "Al parecer la URL ingresada no es correcta")
            labelLoad.grid_remove()
            botonDescargar.config(state="normal")

def dispararHilo():
        thread = Thread(target = comenzarDescarga)
        thread.start()

#Widgets de la ventana
label = Label(ventana, text="Url del video:")
label.grid(row = 0, column = 0, pady = (30, 0))
url = Entry(ventana, bd = 2, width = 50)
url.grid(row = 0, column = 1, pady = (30, 0))
url.focus()
botonDescargar = Button(ventana, text = "Descargar", command = dispararHilo)
botonDescargar.grid(row = 0, column = 2, pady = (30, 0))
labelLoad = Label(ventana, text="Descargando canción...")

labelLoad.grid(row = 1, column = 1, pady = (5, 0))
labelLoad.grid_remove()
ventana.mainloop()
