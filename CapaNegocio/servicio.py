from CapaDatos.repositorio import leer_estudiantes, guardar_estudiantes
from Entidades.estudiante import Estudiante

def agregar_estudiante(nombre, edad, carrera):
    estudiantes = leer_estudiantes()
    nuevo_id = len(estudiantes) + 1
    nuevo = Estudiante(nuevo_id, nombre, edad, carrera)
    estudiantes.append(nuevo)
    guardar_estudiantes(estudiantes)

def obtener_estudiantes():
    return leer_estudiantes()

def eliminar_estudiante(id):
    estudiantes = leer_estudiantes()
    estudiantes = [e for e in estudiantes if e.id != id]
    guardar_estudiantes(estudiantes)