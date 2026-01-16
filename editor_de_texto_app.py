import tkinter as tk
from tkinter import ttk

class EditorDeTextoApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # Configuración de la ventana principal
        self.title("Editor de Texto")
        self.geometry("800x600")

        # Etiqueta de bienvenida
        etiqueta = tk.Label(self, text="Bienvenido a tu editor de texto")
        etiqueta.pack(pady=20)

        # LLamar al método para crear widgets
        self._crear_widgets()

    def _crear_widgets(self) -> None:
        '''Crea los widgets del editor de texto.'''
        # Crear un marco principal
        frame_principal = ttk.Frame(self)
        frame_principal.pack(fill=tk.BOTH, expand=True)
        # Crear una caja de texto con barras de desplazamiento
        scrollbar_vertical = ttk.Scrollbar(frame_principal, orient=tk.VERTICAL)
        scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_horizontal = ttk.Scrollbar(frame_principal, orient=tk.HORIZONTAL)
        scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
        # Crear el widget de texto
        self.texto = tk.Text(
            frame_principal,
            wrap=tk.NONE,
            undo=True,
            yscrollcommand=scrollbar_vertical.set,
            xscrollcommand=scrollbar_horizontal.set,
            font=("Consolas", 12)
        )
        self.texto.pack(fill=tk.BOTH, expand=True)
        # Configurar las barras de desplazamiento
        scrollbar_vertical.config(command=self.texto.yview)
        scrollbar_horizontal.config(command=self.texto.xview)