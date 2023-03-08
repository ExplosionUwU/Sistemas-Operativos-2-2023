import tkinter as tk
import threading

class VentanaContador(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Contador")
        self.pack()
        self.crear_widgets()
        self.contador = 0
        self.hilo_incrementar = None

    def crear_widgets(self):
        # crear el botón para iniciar el contador
        self.boton_iniciar = tk.Button(self, text="Iniciar contador", command=self.iniciar_contador)
        self.boton_iniciar.pack()

        # crear la etiqueta para mostrar el contador
        self.label_contador = tk.Label(self, text="Contador: 0")
        self.label_contador.pack()

    def incrementar_contador(self):
        while True:
            self.contador += 1

    def actualizar_contador(self):
        self.label_contador.config(text="Contador: {}".format(self.contador))
        self.master.after(1000, self.actualizar_contador)

    def iniciar_contador(self):
        # crear el hilo para incrementar el contador
        if not self.hilo_incrementar or not self.hilo_incrementar.is_alive():
            self.hilo_incrementar = threading.Thread(target=self.incrementar_contador)
            self.hilo_incrementar.start()

        # actualizar el valor del contador en la etiqueta
        self.actualizar_contador()

# crear la ventana principal
ventana = tk.Tk()
ventana_contador = VentanaContador(master=ventana)
ventana_contador.mainloop()