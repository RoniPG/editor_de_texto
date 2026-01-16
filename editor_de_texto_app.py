import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from pathlib import Path


class EditorDeTextoApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        # Configuración de la ventana principal
        self.title("Editor de Texto")
        self.geometry("900x600")

        self.archivo_actual: Path | None = None

        # Etiqueta de bienvenida
        etiqueta = tk.Label(self, text="Bienvenido a tu editor de texto")
        etiqueta.pack(pady=20)

        # LLamar al método para crear widgets
        self._crear_widgets()
        self._crear_menu()

    def _crear_widgets(self) -> None:
        """Crea los widgets del editor de texto."""
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
            font=("Consolas", 12),
        )
        self.texto.pack(fill=tk.BOTH, expand=True)
        # Configurar las barras de desplazamiento
        scrollbar_vertical.config(command=self.texto.yview)
        scrollbar_horizontal.config(command=self.texto.xview)

    def _crear_menu(self) -> None:
        """Crea la barra de menú del editor de texto."""
        # Crear la barra de menú
        menu_barra = tk.Menu(self)
        # Creamos el menú Archivo
        menu_archivo = tk.Menu(menu_barra, tearoff=0)
        # Agregamos las opciones al menú Archivo con sus respectivos atajos de teclado
        menu_archivo.add_command(
            label="Nuevo", accelerator="Ctrl+N", command=self.nuevo_archivo
        )
        menu_archivo.add_command(
            label="Abrir...", accelerator="Ctrl+O", command=self.abrir_archivo
        )
        menu_archivo.add_command(
            label="Guardar", accelerator="Ctrl+S", command=self.guardar_archivo
        )
        menu_archivo.add_command(label="Guardar como...", command=self.guardar_como)
        # Separador estetético
        menu_archivo.add_separator()
        menu_archivo.add_command(
            label="Salir", accelerator="Ctrl+Q", command=self.salir
        )
        # Agregamos el menú Archivo a la barra de menú
        menu_barra.add_cascade(label="Archivo", menu=menu_archivo)
        self.config(menu=menu_barra)
        # Atajos de teclado para las opciones del menú
        self.bind("<Control-n>", lambda event: self.nuevo_archivo())
        self.bind("<Control-o>", lambda event: self.abrir_archivo())
        self.bind("<Control-s>", lambda event: self.guardar_archivo())
        self.bind("<Control-q>", lambda event: self.salir())

    def nuevo_archivo(self) -> None:
        """Crea un nuevo archivo de texto."""
        if self._confirmar_guardado():
            self.texto.delete(1.0, tk.END)
            self.archivo_actual = None
            self.actualizar_titulo()

    def abrir_archivo(self) -> None:
        """Abre un archivo de texto existente."""
        if not self._confirmar_guardado():
            return

        ruta_archivo = filedialog.askopenfilename(
            title="Abrir archivo",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
        )
        if not ruta_archivo:
            return

        ruta = Path(ruta_archivo)
        try:
            contenido = ruta.read_text(encoding="utf-8")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir el archivo: {e}")
            return

        self.texto.delete(1.0, tk.END)
        self.texto.insert(1.0, contenido)
        self.archivo_actual = ruta
        self.actualizar_titulo()

    def guardar_archivo(self) -> None:
        """Guarda el archivo de texto actual."""
        if self.archivo_actual is None:
            self.guardar_como()
        else:
            self.guardar_en_ruta(self.archivo_actual)

    def guardar_como(self) -> None:
        """Guarda el archivo de texto actual con un nuevo nombre."""
        ruta_archivo = filedialog.asksaveasfilename(
            title="Guardar como",
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
        )
        if not ruta_archivo:
            return

        ruta = Path(ruta_archivo)
        self.archivo_actual = ruta
        self.guardar_en_ruta(ruta)

    def guardar_en_ruta(self, ruta: Path) -> None:
        """Guarda el contenido del editor en la ruta especificada."""
        contenido = self.texto.get(1.0, tk.END)
        try:
            ruta.write_text(contenido, encoding="utf-8")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
            return

        self.actualizar_titulo()

    def salir(self) -> None:
        """Sale de la aplicación."""
        if self._confirmar_guardado():
            self.destroy()

    def actualizar_titulo(self) -> None:
        """Actualiza el título de la ventana con el nombre del archivo actual."""
        if self.archivo_actual:
            self.title(f"Editor de Texto - {self.archivo_actual.name}")
        else:
            self.title("Editor de Texto - Sin título")

    def _confirmar_guardado(self) -> bool:
        """Pregunta al usuario si desea guardar los cambios antes de continuar."""
        if self.texto.edit_modified():
            respuesta = messagebox.askyesnocancel(
                "Guardar cambios",
                "¿Desea guardar los cambios antes de continuar?",
                default=messagebox.CANCEL,
            )
            if respuesta is None:
                return False
            if respuesta:
                self.guardar_archivo()
        return True


