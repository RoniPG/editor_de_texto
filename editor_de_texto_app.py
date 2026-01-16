import tkinter as tk

class EditorDeTextoApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Editor de Texto")
        self.geometry("800x600")

    