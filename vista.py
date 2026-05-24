from controlador import EjercicioControlador

class EjercicioVista:
    def __init__(self):
        self.controlador = EjercicioControlador()

    def menu_principal(self):
        while True:
            print("\n--- 📦 CRUD EJERCICIOS ---")
            print("1. Crear Ejercicio")
            print("2. Listar Ejercicio")
            print("3. Buscar Ejercicio")
            print("4. Actualizar Ejercicio")
            print("5. Eliminar Ejercicio")
            print("6. Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.vista_crear()
            elif opcion == "2":
                self.vista_listar()
            elif opcion == "3":
                self.vista_buscar()
            elif opcion == "4":
                self.vista_actualizar()
            elif opcion == "5":
                self.vista_eliminar()
            elif opcion == "6":
                print("👋 ¡Hasta luego!")
                break
            else:
                print("⚠ Opción no válida.")

    def vista_crear(self):
        print("\n--- Registrar Ejercicio ---")
        id_ej = int(input("ID: "))
        nombre = input("Nombre: ")
        tipo = input("Tipo: ")
        mensaje = self.controlador.registrar_ejercicio(id_ej, nombre, tipo)
        print(mensaje)

    def vista_listar(self):
        print("\n--- Lista de Ejercicios ---")
        ejercicios = self.controlador.listar_ejercicios()
        if not ejercicios:
            print("No hay ejercicios registrados.")
            return
        for e in ejercicios:
            print(f"ID: {e.id} | {e.nombre} | {e.tipo} ")

    def vista_buscar(self):
        print("\n--- Buscar Ejercicio ---")
        id_ej = int(input("Ingrese el ID a buscar: "))
        e = self.controlador.buscar_ejercicios(id_ej)
        if e:
            print(f"\n🔍 Encontrado -> ID: {e.id} | {e.nombre} | {e.tipo}")
        else:
            print("❌ Entrenamiento no encontrado.")

    def vista_actualizar(self):
        print("\n--- Actualizar Ejercicios ---")
        id_ej = int(input("Ingrese el ID del ejercicio a modificar: "))
        nombre = input("Nuevo Nombre: ")
        tipo = input("Nuevo Tipo: ")
        mensaje = self.controlador.modificar_ejercicio(id_ej, nombre, tipo)
        print(mensaje)

    def vista_eliminar(self):
        print("\n--- Eliminar Ejercicio ---")
        id_ej  = int(input("Ingrese el ID del ejercicio a eliminar: "))
        mensaje = self.controlador.borrar_ejercicio(id_ej)
        print(mensaje)