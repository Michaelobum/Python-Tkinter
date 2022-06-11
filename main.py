from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox


def resource_path(relative_path): #empaquetado de imagenes
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def root():
    def accion(): #accion para descargar los videeos
        enlace = videos.get()
        video = YouTube(enlace)
        descarga = video.streams.get_highest_resolution()
        descarga.download()

    def menu(): #menu flotante
        MessageBox.showinfo("Sobre mí", "Para mas informacion, escribir al: \n+593990066866")

    root = Tk()
    root.config(bd=15)
    root.title("VIDEO DOWNLOADER")
    path = resource_path("icono.ico") #empaquetado de imagenes (python no permite convertir a exe sin empaquetar imagenes)
    root.iconbitmap(path)
    path = resource_path("youtube.png") #empaquetado de imagenes
    imagen = PhotoImage(file=path)
    foto = Label(root, image=imagen, bd=0)
    foto.grid(row=0, column=0) #posición de la foto
    menubar = Menu(root)
    root.config(menu=menubar)
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Contacto", menu=helpmenu)
    helpmenu.add_command(label="Información del autor", command=menu)
    menubar.add_command(label="Salir", command=root.destroy) #detroy es para cerrar la app

    instrucciones = Label(root, text="Programa creado para descargar vídeos de Youtube para 'CYBER MOVIESTRENO'\n")
    instrucciones.grid(row=0, column=1)
    videos = Entry(root) #videos es para el root
    videos.grid(row=1, column=1)
    boton = Button(root, text="Descargar :)", command=accion) #declaracion del boton para descargar
    boton.grid(row=2, column=1)
    root.mainloop()


root()
