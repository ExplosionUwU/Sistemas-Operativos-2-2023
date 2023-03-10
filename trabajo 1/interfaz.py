from tkinter import *
from subprocess import Popen
from tkinter import messagebox
import subprocess
from PIL import Image,ImageTk
import tkinter.font as font
import threading
import time
import schedule

#Interfaz
class App():
   def __init__(self):
      self.ventana=Tk()
      self.ventana.title("Administrador de aplicaiones")
      self.ventana.geometry("1500x700")
      self.ventana.configure(bg='white')

      #widgets
      Fuente = font.Font(size=20)
      fuente2 = font.Font(size=35)
      #Parte 1 interaccion con app
      self.label1 = Label(self.ventana, text="Selecciona una operacion", font=Fuente)
      self.label1.place(x=400, y=20)
      self.label2 = Label(self.ventana, text="Administrador de tareas", font=fuente2)
      self.label2.place(x=330,y=460)
      self.label = Label(self.ventana, text="OFF", font=fuente2)
      self.label.place(x=340,y=560)

      #Parte 3 planificador
      # Iniciar planificador de tareas
      self.ventana.after(10000, self.accionBotonMusica)

      self.ventana.after(10000, self.accionBotonVSC)

      #parte 2 hilos
      #hilo1
      self.numero = 0
      self.label_contador1 = Label(self.ventana, text="contador 1", font=Fuente)
      self.label_contador1.place(x=1080,y=200)

      self.numero2 = 0
      self.label_contador2 = Label(self.ventana, text="contador 2", font=Fuente)
      self.label_contador2.place(x=1280,y=200)

      #botones
      #Parte 1 interaccion con app
      #boton juego 1 offline
      image = Image.open("Imagenes\OsuLogo.png")
      imgJuego1 = ImageTk.PhotoImage(image)
      self.botonJuego1 = Button(self.ventana, width=150, height=150, image=imgJuego1, command=self.accionBotonJuego1)
      self.botonJuego1.place(x=120,y=100)
      #cerrar juego1
      imageClose = Image.open("Imagenes\salirLogo.png")
      imgJuego1Close = ImageTk.PhotoImage(imageClose)
      self.botonCerrarJuego1 = Button(self.ventana, width=50, height=50, image=imgJuego1Close, command=self.accionCerrarJuego1)
      self.botonCerrarJuego1.place(x=120,y=300)

      #boton juego  online
      image2 = Image.open("Imagenes\LolLogo.png")
      imgJuego2 = ImageTk.PhotoImage(image2)
      self.botonJuego2 = Button(self.ventana, width=150, height=150, image=imgJuego2, command=self.accionBotonJuego2)
      self.botonJuego2.place(x=290,y=100)
      #cerrar juego 2
      image2Close = Image.open("Imagenes\salirLogo.png")
      imgJuego12Close = ImageTk.PhotoImage(image2Close)
      self.botonCerrarJuego2 = Button(self.ventana, width=50, height=50, image=imgJuego12Close, command=self.accionCerrarJuego2)
      self.botonCerrarJuego2.place(x=290,y=300)

      #boton musica
      image3 = Image.open("Imagenes\spotifyLogo.png")
      imgMusica = ImageTk.PhotoImage(image3)
      self.botonMusica = Button(self.ventana, width=150, height=150, image=imgMusica, command=self.accionBotonMusica)
      self.botonMusica.place(x=460,y=100)
      #cerrar musica
      image3Close = Image.open("Imagenes\salirLogo.png")
      imgMusicaClose = ImageTk.PhotoImage(image3Close)
      self.botonCerrarMusica = Button(self.ventana, width=50, height=50, image=imgMusicaClose, command=self.accionCerrarMusica)
      self.botonCerrarMusica.place(x=460,y=300)

      #boton Navegador
      image4 = Image.open("Imagenes\chromeLogo.png")
      imgNavegador = ImageTk.PhotoImage(image4)
      self.botonNavegador = Button(self.ventana, width=150, height=150, image=imgNavegador, command=self.accionBotonNavegador)
      self.botonNavegador.place(x=630,y=100)
      #Cerrarnavegador
      image4Close = Image.open("Imagenes\salirLogo.png")
      imgNavegadorClose = ImageTk.PhotoImage(image4Close)
      self.cerrarNavegador = Button(self.ventana, width=50, height=50, image=imgNavegadorClose, command=self.accionCerrarNavegador)
      self.cerrarNavegador.place(x=630,y=300)

      #visual studio code
      image5 = Image.open("Imagenes/blockNotas.png")
      imgVSC = ImageTk.PhotoImage(image5)
      self.botonNavegador = Button(self.ventana, width=150, height=150, image=imgVSC, command=self.accionBotonVSC)
      self.botonNavegador.place(x=800,y=100)
      #cerrar vsc
      image5Close = Image.open("Imagenes\salirLogo.png")
      imgVSCClose = ImageTk.PhotoImage(image5Close)
      self.botoncerrarvsc = Button(self.ventana, width=50, height=50, image=imgVSCClose, command=self.accionCerrarVSC)
      self.botoncerrarvsc.place(x=800,y=300)

      #parte 2 Hilos
      #hilo1
      image6 = Image.open("Imagenes\hilo.png")
      imgHilo1 = ImageTk.PhotoImage(image6)
      self.botonHilo1Go = Button(self.ventana,width=100,height=100, image=imgHilo1, command=self.iniciarHilo1)
      self.botonHilo1Go.place(x=1080,y=260)

      #Hilo2
      image7 = Image.open("Imagenes\hilo.png")
      imgHilo2 = ImageTk.PhotoImage(image7)
      self.botonHilo1Go = Button(self.ventana,width=100,height=100, image=imgHilo2, command=self.iniciarHilo2)
      self.botonHilo1Go.place(x=1280,y=260)

      

      self.ventana.mainloop()
      
   
   #fuciones
   #Parte 1 interaccion con app
   #Juego 1
   def accionBotonJuego1(self):
      juego1 = "C:/Users/ralej/AppData/Local/osulazer/osu!.exe"
      subprocess.Popen([juego1])
      self.contenido_actual = "Osu!.Exe    Running"
      self.label.config(text=self.contenido_actual)

   #cerrar juego 1
   def accionCerrarJuego1(self):
      cerrarJuego1 = "osu!.exe"
      subprocess.call(["taskkill", "/f", "/im", cerrarJuego1])
      self.contenido_actual = "OFF"
      self.label.config(text=self.contenido_actual)

   #Juego2
   def accionBotonJuego2(self):
      juego2 = "C:/Riot Games/Riot Client/RiotClientServices.exe"
      subprocess.Popen([juego2])
      self.contenido_actual = "RiotClientServices.exe    Running"
      self.label.config(text=self.contenido_actual)
   
   #cerrar juego2
   def accionCerrarJuego2(self):
      cerrarJuego2 = "RiotClientServices.exe"
      subprocess.call(["taskkill", "/f", "/im", cerrarJuego2])
      self.contenido_actual = "OFF"
      self.label.config(text=self.contenido_actual)

   #musica
   def accionBotonMusica(self):
      musica = "Spotify.exe"
      subprocess.Popen([musica])
      self.contenido_actual = "Spotify.exe    Running"
      self.label.config(text=self.contenido_actual)

   
      schedule.every(5).seconds.do(self.accionBotonMusica)
      while True:
            # Ejecutar la tarea programada
            schedule.run_pending()


   #cerrar musica
   def accionCerrarMusica(self):
      cerrarMusica = "Spotify.exe"
      subprocess.call(["taskkill", "/f", "/im", cerrarMusica])
      self.contenido_actual = "OFF"
      self.label.config(text=self.contenido_actual)

   #navegador   
   def accionBotonNavegador(self):
      navegador = "C:/Program Files/Google/Chrome/Application/chrome.exe"
      subprocess.Popen([navegador])
      self.contenido_actual = "Chrome.exe    Running"
      self.label.config(text=self.contenido_actual)

   #cerrarNavegador
   def accionCerrarNavegador(self):
      cerrarNavegador = "chrome.exe"
      subprocess.call(["taskkill", "/f", "/im", cerrarNavegador])
      self.contenido_actual = "OFF"
      self.label.config(text=self.contenido_actual)

   #Visual studio code
   def accionBotonVSC(self):
      visualCode = "notepad.exe"
      subprocess.Popen([visualCode])
      self.contenido_actual = "Notepad.exe    Running"
      self.label.config(text=self.contenido_actual)
   #cerrarvsc
   def accionCerrarVSC(self):
      cerrarvsc = "notepad.exe"
      subprocess.call(["taskkill", "/f", "/im", cerrarvsc])
      self.contenido_actual = "OFF"
      self.label.config(text=self.contenido_actual)

   #parte 2 Hilos
   #hilo1
   def actualizar_numero(self):
        self.numero += 1
        self.label_contador1.configure(text=str(self.numero))

   def incrementar_numero(self):
        while True:
            time.sleep(1)
            self.actualizar_numero()

   def iniciarHilo1(self):
        hilo = threading.Thread(target=self.incrementar_numero)
        hilo.start()

   #hilo2
   def actualizar_numero2(self):
        self.numero2 += 1
        self.label_contador2.configure(text=str(self.numero2))

   def incrementar_numero2(self):
        while True:
            time.sleep(1)
            self.actualizar_numero2()

   def iniciarHilo2(self):
        hilo = threading.Thread(target=self.incrementar_numero2)
        hilo.start()

   
       
   
#interfaz principal
ventanaPrincipal=App()



