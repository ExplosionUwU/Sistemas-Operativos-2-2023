import os
import tkinter as tk

# función para abrir Spotify.exe
def open_spotify():
    os.startfile('spotify.exe')

# función para abrir Notepad.exe
def open_notepad():
    os.startfile('notepad.exe')

# Crear ventana principal
root = tk.Tk()
root.geometry('200x100')
root.title('Ejecución de programas')

# Crear botón para iniciar la ejecución de programas
button = tk.Button(root, text='Ejecutar programas', command=lambda: root.after(10000, open_notepad), state=tk.DISABLED)
button.pack(pady=10)

# Crear función para habilitar el botón después de 5 segundos
def enable_button():
    button.configure(state=tk.NORMAL)
    root.after(5000, open_spotify)

# Ejecutar la función de habilitación del botón después de 10 segundos
root.after(10000, enable_button)

# Iniciar la interfaz gráfica
root.mainloop()