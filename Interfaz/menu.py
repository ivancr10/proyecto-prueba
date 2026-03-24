from CapaNegocio.servicio import agregar_estudiante, obtener_estudiantes, eliminar_estudiante

def mostrar_menu():
    print("\n--- Sistema de Estudiantes ---")
    print("1. Agregar estudiante")
    print("2. Ver estudiantes")
    print("3. Eliminar estudiante")
    print("4. Salir")

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            carrera = input("Carrera: ")
            agregar_estudiante(nombre, int(edad), carrera)
            print("✅ Estudiante agregado!")

        elif opcion == "2":
            estudiantes = obtener_estudiantes()
            if not estudiantes:
                print("No hay estudiantes.")
            for e in estudiantes:
                print(f"ID: {e.id} | Nombre: {e.nombre} | Edad: {e.edad} | Carrera: {e.carrera}")

        elif opcion == "3":
            id = int(input("ID del estudiante a eliminar: "))
            eliminar_estudiante(id)
            print("✅ Estudiante eliminado!")

        elif opcion == "4":
            print("Hasta luego!")
            break