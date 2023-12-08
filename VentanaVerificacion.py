import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class VentanaVerification:
    def __init__(self, master):
        self.ventana_verification = master
        self.ventana_verification.title("Verificación")

        # Espacio para la ecuación
        tk.Label(self.ventana_verification, text="Ecuación:", font=("Helvetica", 12)).pack(pady=10)
        tk.Label(self.ventana_verification, text="Aquí se mostrará la ecuación", font=("Helvetica", 12, "italic")).pack()

        # Espacio para la gráfica
        tk.Label(self.ventana_verification, text="Gráfica:", font=("Helvetica", 12)).pack(pady=10)

        # Crear una figura de ejemplo
        self.figura = Figure(figsize=(5, 4), dpi=100)
        self.subplot = self.figura.add_subplot(1, 1, 1)
        self.subplot.plot(np.arange(0, 10, 0.1), np.sin(np.arange(0, 10, 0.1)), label="Ejemplo de gráfica")
        self.subplot.legend()

        # Mostrar la gráfica en la interfaz de Tkinter
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.ventana_verification)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

    def mostrar_ventana(self):
        # Mostrar la ventana
        self.ventana_verification.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaVerification(root)
    root.mainloop()
