import subprocess
from tkinter import *
from subprocess import Popen
import os
from PIL import Image,ImageTk


#Poner imagen en boton
root = Tk()
root.geometry("500x500")

image = Image.open("C:/Users/ralej/Desktop/universidad semestre 7/Sistemas operativos 2/trabajo 1/Imagenes/OsuLogo.png")
img = ImageTk.PhotoImage(image)

btn = Button(root, image=img)
btn.pack()

root.mainloop

#Esta fue gracias cristian
#Juego offline
'''
juego1 = "C:/Users/ralej/AppData/Local/osulazer/osu!.exe"
subprocess.Popen([juego1],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()

#navegador
navegador = "C:/Program Files/Google/Chrome/Application/chrome.exe"
subprocess.Popen([navegador],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()'''
'''
#block de notas
blockNotas = "notepad.exe"
subprocess.Popen([blockNotas],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()

#musica
musica = "Spotify.exe"
subprocess.Popen([musica],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()

juego2 = "C:/Riot Games/Riot Client/RiotClientServices.exe"
subprocess.Popen([juego2],stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True).communicate()
'''
#abrir la app opcional :D
#navegador
#direccionnav = "C:/FromSoftware/Google/Chrome/Application/"
#os.system(direccionnav + 'chrome.exe')
#block de notas
#os.system('notepad')
#musica
#os.system('spotify.exe')
#juego
#direccionLol = 'C:/RiotGames/LeagueofLegends/'
#os.system(direccionLol + 'LeagueClient.exe')

