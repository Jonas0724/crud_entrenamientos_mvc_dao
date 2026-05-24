from dao import EjercicioDAO
from modelo import Ejercicio


class EjercicioControlador:

    def __init__(self):
        self.dao = EjercicioDAO()

    def registrar_ejercicio(
        self,
        id_ej: int,
        nombre: str,
        tipo: str
    ) -> str:
        """
        Registra un nuevo ejercicio.
        """
        if tipo == "":
            return "❌ Error: NO hay ejercicios."

        nuevo_ejercicio = Ejercicio(id_ej, nombre, tipo)

        if self.dao.crear(nuevo_ejercicio):
            return "✅ Ejercicio registrado con éxito."

        return "❌ Error: El ID del ejercicio ya existe."

    def listar_ejercicios(self) -> list:
        """
        Retorna todos los ejercicios registrados.
        """
        return self.dao.obtener_todos()

    def buscar_ejercicios(self, id_ej: int):
        """
        Busca un ejercicio por ID.
        """
        return self.dao.obtener_por_id(id_ej)

    def modificar_ejercicio(
        self,
        id_ej: int,
        nombre: str,
        tipo: str
    ) -> str:
        """
        Modifica un ejercicio existente.
        """
        ejercicio = self.dao.obtener_por_id(id_ej)

        if not ejercicio:
            return "❌ Error: Ejercicio no encontrado."

        ejercicio_actualizado = Ejercicio(id_ej, nombre, tipo)

        if self.dao.actualizar(ejercicio_actualizado):
            return "✅ Ejercicio actualizado con éxito."

        return "❌ Error al actualizar."

    def borrar_ejercicio(self, id_ej: int) -> str:
        """
        Elimina un ejercicio por ID.
        """
        if self.dao.eliminar(id_ej):
            return "✅ Ejercicio eliminado con éxito."

        return "❌ Error: Ejercicio no encontrado."