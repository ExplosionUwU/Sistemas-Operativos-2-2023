import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Gráfica de barras")

# Crear los datos de la gráfica
x = ['Manzanas', 'Naranjas', 'Plátanos', 'Mangos']
y = [25, 10, 15, 20]

# Crear la figura de la gráfica
fig = Figure(figsize=(5, 4), dpi=100)
fig.add_subplot(111).bar(x, y)

# Crear el widget de la gráfica y agregarlo a la ventana de Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()

# Iniciar el loop principal de Tkinter
tk.mainloop()