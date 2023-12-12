import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import sympy
from sympy import symbols, lambdify
from Ventana import Ventana
from VentanaResultados import VentanaResultados
import json

class VentanaVerification(Ventana):
    def __init__(self, alto, ancho, master, ecuacion_var,ventan_anterior):
        super().__init__(alto, ancho, master)
        self.ventana_actual=master
        self.ventana_actual.title("Verificación")
        self.ecuacion_var = ecuacion_var
        self.master.geometry(f"{alto}x{ancho}")
        self.figura, self.subplot = self.crear_figura_subplot()
        self.funcion = self.crear_funcion()
        self.crear_widget()
        Ventana.ventan_anterior=ventan_anterior
        self.metadata=None

    def crear_figura_subplot(self):
        figura = Figure(figsize=(5, 4), dpi=100)
        subplot = figura.add_subplot(1, 1, 1)
        return figura, subplot

    def crear_funcion(self):
        x = symbols('x')
        ecuacion_sym = sympy.sympify(self.ecuacion_var)
        ecuacion_func = lambdify(x, ecuacion_sym, 'numpy')

        # Asegurarse de que la función dependa de x
        return lambda x_vals: ecuacion_func(x_vals) if 'x' in str(ecuacion_sym) else np.full_like(x_vals, ecuacion_func(0))



    def crear_widget(self):
        # Espacio para la ecuación
        tk.Label(self.ventana_actual, text="Ecuación:", font=("Helvetica", 12)).pack(pady=10)
        tk.Label(self.ventana_actual, text=f"{self.ecuacion_var}", font=("Helvetica", 12, "italic")).pack()
        
        # Espacio para la gráfica
        tk.Label(self.ventana_actual, text="Gráfica:", font=("Helvetica", 12)).pack(pady=10)

        # Mostrar la gráfica en la interfaz de Tkinter
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.ventana_actual)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()
        self.actualizar_grafica()

        # Botón "Siguiente"
        tk.Button(self.ventana_actual, text="Siguiente", command=self.mostrar_siguiente, font=("Helvetica", 12)).pack()

        # Botón "Anterior"
        #tk.Button(self.ventana_actual, text="Anterior", command=self.mostrar_anterior, font=("Helvetica", 12)).pack()

    def mostrar_siguiente(self):
        Ventana.ventan_anterior=self
        self.limpiar_widget()
        # Llamar al método para mostrar la ventana VentanaVerification
        if not self.estado_ventana:
            # Limpiar la ventana principal (destruir todos los widgets)
            for widget in self.master.winfo_children():
                widget.destroy()
            self.ventana_proxima = VentanaResultados(self.alto,self.ancho,self.master,self.ecuacion_var,Ventana.ventan_anterior)
            self.ventana_proxima.mostrar_ventana()

    def mostrar_anterior(self):
        pass

    def mostrar_ventana(self):
        # Mostrar la ventana
        self.ventana_actual.deiconify()

    def actualizar_grafica(self):
        self.cargar_metadata_desde_json()
        print(self.metadata[0])
        print(self.metadata[1])
        # Limpiar la figura actual
        self.subplot.clear()

        #print(self.metadata)
        # Graficar la nueva función
        x_vals = np.arange(self.metadata[0],self.metadata[1], 0.1)
        y_vals = self.funcion(x_vals)
        self.subplot.plot(x_vals, y_vals, label=f"Ecuación: {self.ecuacion_var}")
        self.subplot.legend()

        # Actualizar la interfaz de Tkinter
        self.canvas.draw()

    def cargar_metadata_desde_json(self, nombre_archivo='metadata.json'):
        try:
            # Abrir el archivo JSON y cargar los datos
            with open(nombre_archivo, 'r') as archivo_json:
                datos_cargados = json.load(archivo_json)

            # Actualizar self.metadata con los datos cargados
            self.metadata = [
                datos_cargados.get('limite_inferior', 0),
                datos_cargados.get('limite_superior', 0),
                datos_cargados.get('error', 0),
                datos_cargados.get('iteraciones', 0),
                datos_cargados.get('metodo',0)
            ]

            print(f"Datos cargados desde {nombre_archivo}: {self.metadata}")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")
        except json.JSONDecodeError:
            print(f"No se pudo decodificar el contenido del archivo {nombre_archivo}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaVerification(600, 400, root, "2*x")
    root.mainloop()
