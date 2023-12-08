import tkinter as tk
from tkinter import scrolledtext

class VentanaResultados:
    def __init__(self, resultados):
        self.ventana_resultados = tk.Tk()
        self.ventana_resultados.title("Resultados de Métodos Numéricos")

        # Área de texto para mostrar resultados
        self.resultados_text = scrolledtext.ScrolledText(self.ventana_resultados, width=40, height=10, wrap=tk.WORD)
        self.resultados_text.pack(padx=20, pady=20)

        # Mostrar resultados en el área de texto
        for resultado in resultados:
            self.resultados_text.insert(tk.END, resultado + "\n")

if __name__ == "__main__":
    # Ejemplo de uso
    resultados_ejemplo = ["Resultado Método 1: 3.14159", "Resultado Método 2: 2.71828", "Resultado Método 3: 1.61803"]
    VentanaResultados(resultados_ejemplo)
    tk.mainloop()
