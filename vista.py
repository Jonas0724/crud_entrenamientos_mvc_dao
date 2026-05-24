from controlador import EntrenamientoControlador

class EntrenamientoVista:
    def __init__(self):
        self.controlador = EntrenamientoControlador()

    def menu_principal(self):
        while True:
            print("\n--- 📦 CRUD ENTRENAMIENTOS ---")
            print("1. Crear Producto")
            print("2. Listar Productos")
            print("3. Buscar Producto")
            print("4. Actualizar Producto")
            print("5. Eliminar Producto")
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
        print("\n--- Registrar Entrenamiento ---")
        id_ent = int(input("ID: "))
        nombre = input("Nombre: ")
        tipo = input("Tipo: ")
        mensaje = self.controlador.registrar_entrenamiento(id_ent, nombre, tipo)
        print(mensaje)

    def vista_listar(self):
        print("\n--- Lista de Entrenamientos ---")
        entrenamientos = self.controlador.listar_entrenamientos()
        if not entrenamientos:
            print("No hay entrenamientos registrados.")
            return
        for e in entrenamientos:
            print(f"ID: {e.id} | {e.nombre} | {e.tipo} ")

    def vista_buscar(self):
        print("\n--- Buscar Entrenamiento ---")
        id_ent = int(input("Ingrese el ID a buscar: "))
        e = self.controlador.buscar_entrenamiento(id_ent)
        if e:
            print(f"\n🔍 Encontrado -> ID: {e.id} | {e.nombre} | {e.tipo}")
        else:
            print("❌ Entrenamiento no encontrado.")

    def vista_actualizar(self):
        print("\n--- Actualizar Entrenamiento ---")
        id_ent = int(input("Ingrese el ID del entrenamiento a modificar: "))
        nombre = input("Nuevo Nombre: ")
        tipo = input("Nuevo Tipo: ")
        mensaje = self.controlador.modificar_entrenamiento(id_ent, nombre, tipo)
        print(mensaje)

    def vista_eliminar(self):
        print("\n--- Eliminar Entrenamiento ---")
        id_ent  = int(input("Ingrese el ID del entrenamiento a eliminar: "))
        mensaje = self.controlador.borrar_entrenamiento(id_ent)
        print(mensaje)