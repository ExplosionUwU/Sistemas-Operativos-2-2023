import threading
import tkinter as tk

class HiloContador(threading.Thread):
    def __init__(self, label):
        threading.Thread.__init__(self)
        self.label = label
        self.numero = 0
        self.detener = False

    def run(self):
        while not self.detener:
            self.numero += 1
            self.label.config(text=str(self.numero))
    
    def detener_hilo(self):
        self.detener = True

# Crear la interfaz gráfica
root = tk.Tk()
label = tk.Label(root, text="0")
label.pack()