import tkinter as tk
from VentanaVerificacion import VentanaVerification
from Ventana import Ventana

class VentanaPrincipal(Ventana):
    def __init__(self,alto,ancho,master):
        super().__init__(alto,ancho,master)
        
        self.master.title("Calculadora de Métodos Numéricos")
        self.master.geometry(f"{alto}x{ancho}")
        # Variables para almacenar la entrada del usuario
        self.ecuacion_var = tk.StringVar()
        self.metodo_var = tk.StringVar()
        self.error_var = tk.StringVar()

        self.crear_widget()

    def crear_widget(self):
        # Título
        tk.Label(self.ventana_actual, text="Calculadora de Métodos Numéricos", font=("Helvetica", 16, "bold")).grid(row=0, columnspan=2, pady=10)

        # Ecuación
        tk.Label(self.ventana_actual, text="Ecuación:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.ecuacion_var, width=30).grid(row=1, column=1, padx=10)

        # Método Numérico
        tk.Label(self.ventana_actual, text="Método Numérico:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="e")
        metodos = ["Método 1", "Método 2", "Método 3"]
        tk.OptionMenu(self.ventana_actual, self.metodo_var, *metodos).grid(row=2, column=1, padx=10)

        # Error
        tk.Label(self.ventana_actual, text="Error:", font=("Helvetica", 12)).grid(row=3, column=0, sticky="e")
        tk.Entry(self.ventana_actual, textvariable=self.error_var, width=10).grid(row=3, column=1, padx=10)

        tk.Button(self.ventana_actual, text="Siguiente", command=self.mostrar_siguiente, font=("Helvetica", 12)).grid(row=4, columnspan=2, pady=20)


    def mostrar_siguiente(self):
        self.limpiar_widget()
        # Llamar al método para mostrar la ventana VentanaVerification
        if not self.estado_ventana:
            # Limpiar la ventana principal (destruir todos los widgets)
            for widget in self.master.winfo_children():
                widget.destroy()

            self.ventana_siguiente = VentanaVerification(self.alto,self.ancho,self.master,self.ecuacion_var)
            self.ventana_siguiente.mostrar_ventana()

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(600,400,root)
    root.mainloop()
