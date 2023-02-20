from tkinter import *
from subprocess import Popen
from tkinter import messagebox
import subprocess
from PIL import Image,ImageTk
import tkinter.font as font


#Interfaz
class App():
   def __init__(self):
      ventana=Tk()
      ventana.title("Administrador de aplicaiones")
      ventana.geometry("1080x700")
      ventana.configure(bg='white')

      #widgets
      Fuente = font.Font(size=20)
      self.label1 = Label(ventana, text="Selecciona una operacion", font=Fuente)
      self.label1.place(x=400, y=20)
      #botones
      #boton juego 1 offline
      image = Image.open("C:/Users/ralej/Desktop/universidad semestre 7/Sistemas operativos 2/trabajo 1/Imagenes/OsuLogo.png")
      imgJuego1 = ImageTk.PhotoImage(image)
      self.botonJuego1 = Button(ventana, width=150, height=150, image=imgJuego1, command=self.accionBotonJuego1)
      self.botonJuego1.place(x=120,y=100)

      #boton juego  online
      image2 = Image.open("C:/Users/ralej/Desktop/universidad semestre 7/Sistemas operativos 2/trabajo 1/Imagenes/LolLogo.png")
      imgJuego2 = ImageTk.PhotoImage(image2)
      self.botonJuego2 = Button(ventana, width=150, height=150, image=imgJuego2, command=self.accionBotonJuego2)
      self.botonJuego2.place(x=290,y=100)

      #boton musica
      image3 = Image.open("C:/Users/ralej/Desktop/universidad semestre 7/Sistemas operativos 2/trabajo 1/Imagenes/spotifyLogo.png")
      imgMusica = ImageTk.PhotoImage(image3)
      self.botonMusica = Button(ventana, width=150, height=150, image=imgMusica, command=self.accionBotonMusica)
      self.botonMusica.place(x=460,y=100)

      #boton Navegador
      image4 = Image.open("C:/Users/ralej/Desktop/universidad semestre 7/Sistemas operativos 2/trabajo 1/Imagenes/chromeLogo.png")
      imgNavegador = ImageTk.PhotoImage(image4)
      self.botonNavegador = Button(ventana, width=150, height=150, image=imgNavegador, command=self.accionBotonNavegador)
      self.botonNavegador.place(x=630,y=100)

      #visual studio code
      image5 = Image.open("C:/Users/ralej/Desktop/universidad semestre 7/Sistemas operativos 2/trabajo 1/Imagenes/VSC.png")
      imgVSC = ImageTk.PhotoImage(image5)
      self.botonNavegador = Button(ventana, width=150, height=150, image=imgVSC, command=self.accionBotonVSC)
      self.botonNavegador.place(x=800,y=100)


      ventana.mainloop()

   #fuciones
   #Juego 1
   def accionBotonJuego1(self):
      juego1 = "C:/Users/ralej/AppData/Local/osulazer/osu!.exe"
      subprocess.Popen([juego1],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()
      messagebox.showinfo(message="Se ejecuro OSU!")

   #Juego2
   def accionBotonJuego2(self):
      juego2 = "C:/Riot Games/Riot Client/RiotClientServices.exe"
      subprocess.Popen([juego2],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()
      messagebox.showinfo(message="Se ejecuro RiotGames")

   #musica
   def accionBotonMusica(self):
      musica = "Spotify.exe"
      subprocess.Popen([musica],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()
      messagebox.showinfo(message="Se ejecuro Spotify")

   #navegador   
   def accionBotonNavegador(self):
      navegador = "C:/Program Files/Google/Chrome/Application/chrome.exe"
      subprocess.Popen([navegador],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()
      messagebox.showinfo(message="Se ejecuro Google Chrome")

   #Visual studio code
   def accionBotonVSC(self):
      visualCode = "C:/Users/ralej/AppData/Local/Programs/Microsoft VS Code/Code.exe"
      subprocess.Popen([visualCode],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()
      messagebox.showinfo(message="Se ejecuro Visual Studio Code")

   
#interfaz principal
ventanaPrincipal=App()

