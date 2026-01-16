# 📝 Editor de Texto en Python

Editor de texto sencillo desarrollado en **Python** utilizando **Tkinter**.  
El objetivo del proyecto es practicar la creación de interfaces gráficas (GUI) y la gestión de archivos, simulando las funcionalidades básicas de un editor de texto real.

---

## 🚀 Características

- Interfaz gráfica simple e intuitiva
- Área de texto para escribir y editar contenido
- Crear un archivo nuevo
- Abrir archivos de texto (`.txt`)
- Guardar archivos
- Guardar archivos con un nuevo nombre
- Barra de menú con opciones básicas

---

## 🧠 Tecnologías utilizadas

- **Python 3**
- **Tkinter** (incluido en la instalación estándar de Python)

---

## 📂 Estructura del proyecto

```
text_editor/
│
├─ main.py
├─ editor_de_texto_app.py 
├─ README.md
```


---

## ⚙️ Instalación

#### 1. Asegúrate de tener **Python 3.10 o superior** instalado.

1. 1  (Opcional) Crear un entorno virtual con conda

   ```
    conda create -n  python=3.11
    conda activate escritura_veloz_env
   ```

#### 2. Clona el repositorio:

   ```
   git clone https://github.com/RoniPG/editor_de_texto.git
   ```

#### 3. Accede al directorio del proyecto:

    ```
    cd editor_de_texto
    ```

#### 4. Ejecuta la aplicación:

    ```
    python main.py
    ```

> Tkinter viene incluido por defecto con Python, no es necesario instalar dependencias adicionales.

---

## 🎮 Cómo usar el editor

- Archivo → Nuevo: Crea un documento en blanco.

- Archivo → Abrir: Abre un archivo de texto existente.

- Archivo → Guardar: Guarda el archivo actual.

- Archivo → Guardar como: Guarda el archivo con otro nombre o ubicación.

- Archivo → Salir: Cierra la aplicación.

---

## 📌 Estado del proyecto

✔ MVP completado
El editor es totalmente funcional para tareas básicas de edición de texto.

---

## 🔮 Posibles mejoras futuras

- Deshacer / Rehacer

- Copiar, cortar y pegar
 
- Selector de fuente y tamaño de texto
 
- Modo oscuro
 
- Buscador de texto
