from dao import EntrenamientoDAO
from modelo import Entrenamiento

class EntrenamientoControlador:
    def __init__(self):
        self.dao = EntrenamientoDAO()

    def registrar_entrenamiento(self, id_ent: int, nombre: str, tipo: str) -> str:
        if tipo == "":
             return "❌ Error: NO hay entrenamientos."
        
        nuevo_entrenamiento = Entrenamiento(id_ent, nombre, tipo)
        if self.dao.crear(nuevo_entrenamiento):
            return "✅ Entrenamiento registrado con éxito."
        return "❌ Error: El ID del entrenamiento ya existe."

    def listar_entrenamientos(self):
        return self.dao.obtener_todos()

    def buscar_entrenamiento(self, id_ent: int):
        return self.dao.obtener_por_id(id_ent)

    def modificar_entrenamiento(self, id_ent: int, nombre: str, tipo: str) -> str:
        ent = self.dao.obtener_por_id(id_ent)
        if not ent:
            return "❌ Error: Entrenamiento no encontrado."
        
        ent_actualizado = Entrenamiento(id_ent, nombre, tipo)
        if self.dao.actualizar(ent_actualizado):
            return "✅ Producto actualizado con éxito."
        return "❌ Error al actualizar."

    def borrar_entrenamiento(self, id_ent: int) -> str:
        if self.dao.eliminar(id_ent):
            return "✅ Entrenamiento eliminado con éxito."
        return "❌ Error: Entrenamiento no encontrado."