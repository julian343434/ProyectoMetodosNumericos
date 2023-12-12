import tkinter as tk
from VentanaVerificacion import VentanaVerification
from Ventana import Ventana
import json


class VentanaPrincipal(Ventana):
    def __init__(self, alto, ancho, master):
        super().__init__(alto, ancho, master)

        self.metadata=None
        self.master.title("Calculadora de Métodos Numéricos")
        self.master.geometry(f"{alto}x{ancho}")
        # Variables para almacenar la entrada del usuario
        self.ecuacion_var = tk.StringVar()
        self.metodo_var = tk.StringVar()
        self.error_var = tk.StringVar()
        self.limite_inferior=tk.StringVar()
        self.limite_superior=tk.StringVar()
        self.iteraciones=tk.StringVar()
        self.widgets_metodo_especifico = []  # Lista para almacenar widgets específicos del método

        self.crear_widget()


    def crear_widget(self):
        # Título
        tk.Label(self.ventana_actual, text="Calculadora de Métodos Numéricos", font=("Helvetica", 16, "bold")).grid(row=0, columnspan=2, pady=10)

        # Ecuación
        tk.Label(self.ventana_actual, text="Ecuación:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.ecuacion_var, width=30).grid(row=1, column=1, padx=10)

        # Método Numérico
        tk.Label(self.ventana_actual, text="Método Numérico:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="e")
        metodos = ["biseccion", "falsa posicion", "secante","Newthon Rapson Mejorado"]
        tk.OptionMenu(self.ventana_actual, self.metodo_var, *metodos, command=self.actualizar_widgets_metodo).grid(row=2, column=1, padx=10)

        # Botón para mostrar el siguiente paso
        tk.Button(self.ventana_actual, text="Siguiente", command=self.mostrar_siguiente, font=("Helvetica", 12)).grid(row=8, columnspan=3, pady=20)

    def actualizar_widgets_metodo(self, *_):
        # Limpia los widgets anteriores
        self.limpiar_widget()

        # Lógica para crear widgets específicos del método seleccionado
        metodo_seleccionado = self.metodo_var.get()
        if metodo_seleccionado == "biseccion":
            self.crear_widgets_metodo1()
        elif metodo_seleccionado == "falsa posicion":
            self.crear_widgets_metodo2()
        elif metodo_seleccionado == "secante":
            self.crear_widgets_metodo3()
        elif metodo_seleccionado == "Newthon Rapson Mejorado":
            self.crear_widgets_metodo4()

    def crear_widgets_metodo1(self):
        self.metadata = [None] * 5  # Inicializar metadata con valores nulos

        # Crea y coloca widgets específicos para el Método 1
        tk.Label(self.ventana_actual, text="Límite Inferior (Xo):", font=("Helvetica", 12)).grid(row=3, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.limite_inferior, width=10).grid(row=3, column=1, padx=10)

        tk.Label(self.ventana_actual, text="Límite Superior (Xl):", font=("Helvetica", 12)).grid(row=4, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.limite_superior, width=10).grid(row=4, column=1, padx=10)

        tk.Label(self.ventana_actual, text="Error:", font=("Helvetica", 12)).grid(row=5, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.error_var, width=10).grid(row=5, column=1, padx=10)

        tk.Label(self.ventana_actual, text="Máxima Iteraciones:", font=("Helvetica", 12)).grid(row=6, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.iteraciones, width=10).grid(row=6, column=1, padx=10)

        # Botón para capturar los datos
        tk.Button(self.ventana_actual, text="Capturar Datos", command=self.capturar_datos_metodo1, font=("Helvetica", 12)).grid(row=7, columnspan=2, pady=10)

    def capturar_datos_metodo1(self):
        # Capturar los datos en metadata
        try:
            self.metadata[0] = int(self.limite_inferior.get())
            self.metadata[1] = int(self.limite_superior.get())
            self.metadata[2] = int(self.error_var.get())
            self.metadata[3] = int(self.iteraciones.get())
            self.metadata[4] = str(self.metodo_var.get())
        except ValueError:
            print("Por favor, ingrese valores numéricos en todos los campos.")
            return

        # Puedes realizar acciones adicionales aquí si es necesario

        # Mostrar un mensaje o continuar con la lógica de tu aplicación
        self.guardar_metadata_en_json(nombre_archivo='metadata.json')

    def capturar_datos_metodo2(self):
        # Capturar los datos en metadata
        try:
            self.metadata[0] = int(self.limite_inferior.get())
            self.metadata[1] = 0
            self.metadata[2] = int(self.error_var.get())
            self.metadata[3] = int(self.iteraciones.get())
            self.metadata[4] = str(self.metodo_var.get())
        except ValueError:
            print("Por favor, ingrese valores numéricos en todos los campos.")
            return

        # Puedes realizar acciones adicionales aquí si es necesario

        # Mostrar un mensaje o continuar con la lógica de tu aplicación
        self.guardar_metadata_en_json(nombre_archivo='metadata.json')
        
    def crear_widgets_metodo2(self):
        self.metadata = [None] * 5
        # Crea y coloca widgets específicos para el Método 2
        tk.Label(self.ventana_actual, text="Límite Inferior (Xo):", font=("Helvetica", 12)).grid(row=3, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.limite_inferior, width=10).grid(row=3, column=1, padx=10)
        self.metadata.append(self.limite_inferior.get())

        tk.Label(self.ventana_actual, text="Límite Superior (Xl):", font=("Helvetica", 12)).grid(row=4, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.limite_superior, width=10).grid(row=4, column=1, padx=10)
        self.metadata.append(self.limite_superior.get())

        tk.Label(self.ventana_actual, text="Error:", font=("Helvetica", 12)).grid(row=5, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.error_var, width=10).grid(row=5, column=1, padx=10)
        self.metadata.append(self.error_var.get())

        tk.Label(self.ventana_actual, text="Máxima Iteraciones:", font=("Helvetica", 12)).grid(row=6, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.iteraciones, width=10).grid(row=6, column=1, padx=10)
        self.metadata.append(self.iteraciones.get())

        # Botón para capturar los datos
        tk.Button(self.ventana_actual, text="Capturar Datos", command=self.capturar_datos_metodo1, font=("Helvetica", 12)).grid(row=7, columnspan=2, pady=10)

    def crear_widgets_metodo3(self):
        self.metadata = [None] * 5
        # Crea y coloca widgets específicos para el Método 2
        tk.Label(self.ventana_actual, text="punto inicial:", font=("Helvetica", 12)).grid(row=3, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.limite_inferior, width=10).grid(row=3, column=1, padx=10)
        self.metadata.append(self.limite_inferior.get())

        tk.Label(self.ventana_actual, text="punto final:", font=("Helvetica", 12)).grid(row=4, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.limite_superior, width=10).grid(row=4, column=1, padx=10)
        self.metadata.append(self.limite_superior.get())

        tk.Label(self.ventana_actual, text="Error:", font=("Helvetica", 12)).grid(row=5, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.error_var, width=10).grid(row=5, column=1, padx=10)
        self.metadata.append(self.error_var.get())

        tk.Label(self.ventana_actual, text="Máxima Iteraciones:", font=("Helvetica", 12)).grid(row=6, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.iteraciones, width=10).grid(row=6, column=1, padx=10)
        self.metadata.append(self.iteraciones.get())

        # Botón para capturar los datos
        tk.Button(self.ventana_actual, text="Capturar Datos", command=self.capturar_datos_metodo1, font=("Helvetica", 12)).grid(row=7, columnspan=2, pady=10)

    def crear_widgets_metodo4(self):
        self.metadata = [None] * 5
        # Crea y coloca widgets específicos para el Método 2
        tk.Label(self.ventana_actual, text="valor inicial:", font=("Helvetica", 12)).grid(row=3, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.limite_inferior, width=10).grid(row=3, column=1, padx=10)
        self.metadata.append(self.limite_inferior.get())

        tk.Label(self.ventana_actual, text="Error:", font=("Helvetica", 12)).grid(row=5, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.error_var, width=10).grid(row=5, column=1, padx=10)
        self.metadata.append(self.error_var.get())

        tk.Label(self.ventana_actual, text="Máxima Iteraciones:", font=("Helvetica", 12)).grid(row=6, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.iteraciones, width=10).grid(row=6, column=1, padx=10)
        self.metadata.append(self.iteraciones.get())

        tk.Button(self.ventana_actual, text="Capturar Datos", command=self.capturar_datos_metodo2, font=("Helvetica", 12)).grid(row=7, columnspan=2, pady=10)

    def limpiar_widget(self):
        # Limpiar widgets específicos del método
        for widget in self.widgets_metodo_especifico:
            try:
                widget.destroy()
            except tk.TclError:
                pass
        self.widgets_metodo_especifico = []

    def mostrar_metodos(self):
        pass

    def mostrar_siguiente(self):
        Ventana.ventan_anterior=self
        metadata=self.metadata
        self.limpiar_widget()
        # Llamar al método para mostrar la ventana VentanaVerification
        if not self.estado_ventana:
            # Limpiar la ventana principal (destruir todos los widgets)
            for widget in self.master.winfo_children():
                widget.destroy()
            
            self.ventana_proxima = VentanaVerification(self.alto,self.ancho,self.master,str(self.ecuacion_var.get()),Ventana.ventan_anterior)
            self.ventana_proxima.mostrar_ventana()

    def guardar_metadata_en_json(self, nombre_archivo='metadata.json'):
        # Obtener el contenido de self.metadata
        metadata = self.metadata

        # Verificar si hay datos en metadata antes de guardar
        if metadata:
            # Crear un diccionario con la información que deseas almacenar
            datos_guardar = {
                'limite_inferior': metadata[0],
                'limite_superior': metadata[1],
                'error': metadata[2],
                'iteraciones': metadata[3],
                'metodo':metadata[4]
            }

            # Crear o abrir el archivo JSON y escribir los datos
            with open(nombre_archivo, 'w') as archivo_json:
                json.dump(datos_guardar, archivo_json)

            print(f"Datos guardados en {nombre_archivo}")
        else:
            print("No hay datos en metadata para guardar.")

    def mostrar_anterior(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(1000,1000,root)
    root.mainloop()
