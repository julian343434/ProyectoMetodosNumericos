import tkinter as tk

class VentanaVerification:
    def __init__(self, master):
        self.ventana_verification = master
        self.ventana_verification.title("Verificación")

        # Espacio para la ecuación
        tk.Label(self.ventana_verification, text="Ecuación:", font=("Helvetica", 12)).pack(pady=10)
        tk.Label(self.ventana_verification, text="Aquí se mostrará la ecuación", font=("Helvetica", 12, "italic")).pack()

        # Espacio para la gráfica
        tk.Label(self.ventana_verification, text="Gráfica:", font=("Helvetica", 12)).pack(pady=10)
        tk.Label(self.ventana_verification, text="Aquí se mostrará la gráfica", font=("Helvetica", 12, "italic")).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaVerification(root)
    root.mainloop()
