import json
import os
from Entidades.estudiante import Estudiante

ARCHIVO = "CapaDatos/estudiantes.json"

def leer_estudiantes():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, "r") as f:
        datos = json.load(f)
    return [Estudiante(d["id"], d["nombre"], d["edad"], d["carrera"]) for d in datos]

def guardar_estudiantes(estudiantes):
    datos = [{"id": e.id, "nombre": e.nombre, "edad": e.edad, "carrera": e.carrera} for e in estudiantes]
    with open(ARCHIVO, "w") as f:
        json.dump(datos, f, indent=4)