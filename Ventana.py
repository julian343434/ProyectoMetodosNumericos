import tkinter as tk

class Ventana(tk.Tk) :
    ventana_proxima=None
    ventan_anterior=None
    ventana_actual=None
    def __init__(self,alto,ancho,master):
        self.alto=alto
        self.ancho=ancho
        self.master = master
        self.estado_ventana=None
        self.master.geometry(f"{alto}x{ancho}")

        self.ventana_actual = tk.Frame(self.master, padx=20, pady=20)
        self.ventana_actual.pack()

    def limpiar_widget(self):
        # Limpiar la ventana principal (destruir todos los widgets)
        self.estado_ventana=False
        for widget in self.master.winfo_children():
                widget.destroy()   

    def mostrar_siguiente(self):
        pass
            
    def mostrar_ventana(self):
        self.ventana_actual.deiconify()

    def crear_widget(self):
        pass 

    def mostrar_anterior(self):
        pass

    def configurar_ventana(self):
        pass
