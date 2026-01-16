import tkinter as tk

class EditorDeTextoApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Editor de Texto")
        self.geometry("800x600")

        # Etiqueta de bienvenida
        etiqueta = tk.Label(self, text="Bienvenido a tu editor de texto")
        etiqueta.pack(pady=20)
