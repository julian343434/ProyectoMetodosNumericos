import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from Ventana import Ventana

class VentanaVerification(Ventana):
    def __init__(self,alto,ancho,master,ecuacion_var):
        super().__init__(alto,ancho,master)
        self.ventana_actual = master
        self.ventana_actual.title("Verificación")
        self.ecuacion_var=ecuacion_var
        self.master.geometry(f"{alto}x{ancho}")

        self.crear_widget()

    def crear_widget(self):
        # Espacio para la ecuación
        tk.Label(self.ventana_actual, text="Ecuación:", font=("Helvetica", 12)).pack(pady=10)
        tk.Label(self.ventana_actual, text=f"{self.ecuacion_var}", font=("Helvetica", 12, "italic")).pack()
        # Espacio para la gráfica
        tk.Label(self.ventana_actual, text="Gráfica:", font=("Helvetica", 12)).pack(pady=10)
        # Crear una figura de ejemplo
        self.figura = Figure(figsize=(5, 4), dpi=100)
        self.subplot = self.figura.add_subplot(1, 1, 1)
        self.subplot.plot(np.arange(0, 10, 0.1), np.sin(np.arange(0, 10, 0.1)), label="Ejemplo de gráfica")
        self.subplot.legend()
        # Mostrar la gráfica en la interfaz de Tkinter
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.ventana_actual)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()
        # Botón "Siguiente"
        tk.Button(self.ventana_actual, text="Siguiente", command=self.mostrar_siguiente, font=("Helvetica", 12)).grid(row=4, columnspan=2, pady=20)
        # Botón "Anterior"
        tk.Button(self.ventana_actual, text="Siguiente", command=self.mostrar_siguiente, font=("Helvetica", 12)).grid(row=4, columnspan=2, pady=20)
    
    def mostrar_ventana(self):
        # Mostrar la ventana
        self.ventana_actual.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaVerification(600,400,root,"2x")
    root.mainloop()
