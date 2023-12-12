import tkinter as tk
from tkinter import scrolledtext
from Ventana import Ventana
from ProyectoFinal import MetodosNumericos
import json


class VentanaResultados(Ventana):
    def __init__(self,alto, ancho, master,ecuacion_var,ventan_anterior):

        super().__init__(alto, ancho, master)
        self.ventana_actual=master
        self.ventana_actual.title("Resultados de Métodos Numéricos")
        self.ecuacion_var = ecuacion_var
        self.master.geometry(f"{alto}x{ancho}")
        self.metadata=None
        self.raiz=MetodosNumericos(self.ecuacion_var)
        self.raices_var=None
        Ventana.ventan_anterior=ventan_anterior

        self.crear_widget()



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
    
    def crear_widget(self):
        self.cargar_metadata_desde_json()

        # Lógica para crear widgets específicos del método seleccionado
        metodo_seleccionado = self.metadata[4]
        if metodo_seleccionado == "biseccion":
            self.raices_var = self.raiz.biseccion(self.metadata[0], self.metadata[1], self.metadata[2], self.metadata[3])
        elif metodo_seleccionado == "falsa posicion":
            self.raices_var = self.raiz.falsa_posicion(self.metadata[0], self.metadata[1], self.metadata[2], self.metadata[3])
        elif metodo_seleccionado == "secante":
            self.raices_var = self.raiz.secante(self.metadata[0], self.metadata[1], self.metadata[2], self.metadata[3])
        elif metodo_seleccionado == "Newthon Rapson Mejorado":
            self.raices_var = self.raiz.newton_raphson_mejorado(self.metadata[0], self.metadata[2], self.metadata[3])

        # Área de texto para la ecuación
        tk.Label(self.ventana_actual, text="Ecuación:").pack()
        self.ecuacion_text = scrolledtext.ScrolledText(self.ventana_actual, wrap=tk.WORD, width=40, height=5)
        self.ecuacion_text.insert(tk.END, str(self.ecuacion_var))  # Insertar el contenido de la ecuación
        self.ecuacion_text.config(state=tk.DISABLED)  # Deshabilitar la edición
        self.ecuacion_text.pack()

        # Área de texto para las raíces encontradas
        tk.Label(self.ventana_actual, text="Raíces encontradas:").pack()
        self.raices_text = scrolledtext.ScrolledText(self.ventana_actual, wrap=tk.WORD, width=40, height=10)
        self.raices_text.insert(tk.END, str(self.raices_var))  # Insertar el contenido de las raíces
        self.raices_text.config(state=tk.DISABLED)  # Deshabilitar la edición
        self.raices_text.pack()


        

if __name__ == "__main__":
    # Ejemplo de uso
    resultados_ejemplo = ["Resultado Método 1: 3.14159", "Resultado Método 2: 2.71828", "Resultado Método 3: 1.61803"]
    VentanaResultados(resultados_ejemplo)
    tk.mainloop()
