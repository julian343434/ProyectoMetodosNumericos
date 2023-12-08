import tkinter as tk
from VentanaVerificacion import VentanaVerification

class VentanaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora de Métodos Numéricos")

        # Variables para almacenar la entrada del usuario
        self.ecuacion_var = tk.StringVar()
        self.metodo_var = tk.StringVar()
        self.error_var = tk.StringVar()

        # Ventana 1
        self.ventana1 = tk.Frame(self.master, padx=20, pady=20)
        self.ventana1.pack()

        # Título
        tk.Label(self.ventana1, text="Calculadora de Métodos Numéricos", font=("Helvetica", 16, "bold")).grid(row=0, columnspan=2, pady=10)

        # Ecuación
        tk.Label(self.ventana1, text="Ecuación:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="e")
        tk.Entry(self.ventana1, textvariable=self.ecuacion_var, width=30).grid(row=1, column=1, padx=10)

        # Método Numérico
        tk.Label(self.ventana1, text="Método Numérico:", font=("Helvetica", 12)).grid(row=2, column=0, sticky="e")
        metodos = ["Método 1", "Método 2", "Método 3"]
        tk.OptionMenu(self.ventana1, self.metodo_var, *metodos).grid(row=2, column=1, padx=10)

        # Error
        tk.Label(self.ventana1, text="Error:", font=("Helvetica", 12)).grid(row=3, column=0, sticky="e")
        tk.Entry(self.ventana1, textvariable=self.error_var, width=10).grid(row=3, column=1, padx=10)

        # Botón "Siguiente"
        tk.Button(self.ventana1, text="Siguiente", command=self.mostrar_ventana2, font=("Helvetica", 12)).grid(row=4, columnspan=2, pady=20)
        self.ventana_verification = None  # Inicializar como None

    def mostrar_ventana2(self):
        # Llamar al método para mostrar la ventana VentanaVerification
        if not self.ventana_verification:
            # Limpiar la ventana principal (destruir todos los widgets)
            for widget in self.master.winfo_children():
                widget.destroy()

            # Crear e inicializar la instancia de VentanaVerification
            self.ventana_verification = VentanaVerification(self.master)
            self.ventana_verification.mostrar_ventana()

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()