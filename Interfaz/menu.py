import tkinter as tk
from tkinter import ttk, messagebox
 
# Simulación de la capa de negocio (reemplazá con tu import real)
# from CapaNegocio.servicio import agregar_estudiante, obtener_estudiantes, eliminar_estudiante
 
# ─── Simulación temporal para prueba ───────────────────────────────────────────
estudiantes_db = []
contador_id = [1]
 
def agregar_estudiante(nombre, edad, carrera):
    estudiantes_db.append({
        "id": contador_id[0],
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    })
    contador_id[0] += 1
 
def obtener_estudiantes():
    return estudiantes_db
 
def eliminar_estudiante(id):
    global estudiantes_db
    estudiantes_db = [e for e in estudiantes_db if e["id"] != id]
# ───────────────────────────────────────────────────────────────────────────────
 
 
class AppEstudiantes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Estudiantes")
        self.geometry("650x480")
        self.resizable(False, False)
        self.configure(bg="#f0f2f5")
        self._construir_ui()
 
    def _construir_ui(self):
        # ── Título ──────────────────────────────────────────────────────────────
        tk.Label(
            self, text="Sistema de Estudiantes",
            font=("Helvetica", 16, "bold"),
            bg="#f0f2f5", fg="#1a1a2e"
        ).pack(pady=(16, 4))
 
        # ── Formulario ──────────────────────────────────────────────────────────
        frame_form = tk.LabelFrame(
            self, text="Nuevo estudiante",
            font=("Helvetica", 10), bg="#f0f2f5", fg="#333", padx=12, pady=8
        )
        frame_form.pack(padx=20, fill="x")
 
        campos = [("Nombre:", 0), ("Edad:", 1), ("Carrera:", 2)]
        self.entradas = {}
 
        for label, col in campos:
            tk.Label(frame_form, text=label, bg="#f0f2f5", font=("Helvetica", 10)).grid(
                row=0, column=col * 2, padx=(0, 4), pady=6, sticky="e"
            )
            entrada = tk.Entry(frame_form, width=18, font=("Helvetica", 10))
            entrada.grid(row=0, column=col * 2 + 1, padx=(0, 12))
            self.entradas[label.replace(":", "").lower()] = entrada
 
        tk.Button(
            frame_form, text="➕ Agregar", command=self._agregar,
            bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"),
            relief="flat", padx=10, cursor="hand2"
        ).grid(row=0, column=6, padx=(4, 0))
 
        # ── Tabla ───────────────────────────────────────────────────────────────
        frame_tabla = tk.Frame(self, bg="#f0f2f5")
        frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)
 
        columnas = ("ID", "Nombre", "Edad", "Carrera")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=12)
 
        anchos = {"ID": 50, "Nombre": 200, "Edad": 70, "Carrera": 200}
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=anchos[col], anchor="center")
 
        scroll = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
 
        # ── Botón eliminar ───────────────────────────────────────────────────────
        tk.Button(
            self, text="🗑 Eliminar seleccionado", command=self._eliminar,
            bg="#e53935", fg="white", font=("Helvetica", 10, "bold"),
            relief="flat", padx=10, pady=4, cursor="hand2"
        ).pack(pady=(0, 12))
 
        self._actualizar_tabla()
 
    # ── Acciones ─────────────────────────────────────────────────────────────────
    def _agregar(self):
        nombre  = self.entradas["nombre"].get().strip()
        edad    = self.entradas["edad"].get().strip()
        carrera = self.entradas["carrera"].get().strip()
 
        if not nombre or not edad or not carrera:
            messagebox.showwarning("Campos incompletos", "Por favor completá todos los campos.")
            return
 
        if not edad.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número.")
            return
 
        agregar_estudiante(nombre, int(edad), carrera)
 
        for e in self.entradas.values():
            e.delete(0, tk.END)
 
        self._actualizar_tabla()
        messagebox.showinfo("Éxito", "✅ Estudiante agregado correctamente.")
 
    def _eliminar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Sin selección", "Seleccioná un estudiante de la tabla.")
            return
 
        id_estudiante = int(self.tabla.item(seleccion[0])["values"][0])
        confirmar = messagebox.askyesno("Confirmar", "¿Seguro que querés eliminar este estudiante?")
 
        if confirmar:
            eliminar_estudiante(id_estudiante)
            self._actualizar_tabla()
 
    def _actualizar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
 
        for e in obtener_estudiantes():
            self.tabla.insert("", "end", values=(e["id"], e["nombre"], e["edad"], e["carrera"]))
 
 
