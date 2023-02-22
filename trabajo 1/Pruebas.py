import tkinter as tk

class MyApp:
    def __init__(self):
        # Crear ventana y elementos de interfaz
        self.ventana = tk.Tk()
        self.label = tk.Label(self.ventana, text="Contenido inicial")
        self.boton = tk.Button(self.ventana, text="Actualizar", command=self.actualizar_label)
        
        # Variables de control
        self.contenido_actual = "Contenido inicial"
        
        # Colocar elementos de interfaz en la ventana
        self.label.pack()
        self.boton.pack()
        
    def actualizar_label(self):
        # Actualizar el contenido del label
        self.contenido_actual = "Contenido actualizado"
        self.label.config(text=self.contenido_actual)
        
    def run(self):
        # Ejecutar el programa
        self.ventana.mainloop()

# Crear instancia de la aplicación y ejecutarla
app = MyApp()
app.run()
