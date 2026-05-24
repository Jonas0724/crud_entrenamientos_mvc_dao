import json
import os
from typing import List, Optional
from modelo import Entrenamiento

class EntrenamientoDAO:
    def __init__(self, archivo_db="bd.json"):
        self.archivo_db = archivo_db
        self._inicializar_bd()

    def _inicializar_bd(self):
        """Crea el archivo JSON si no existe."""
        if not os.path.exists(self.archivo_db):
            with open(self.archivo_db, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _leer_todos(self) -> List[dict]:
        with open(self.archivo_db, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _guardar_todos(self, datos: List[dict]):
        with open(self.archivo_db, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4)

    # === OPERACIONES CRUD ===

    def crear(self, entrenamiento: Entrenamiento) -> bool:
        datos = self._leer_todos()
        # Verificar que el ID no exista
        if any(e['id'] == entrenamiento.id for e in datos):
            return False
        datos.append(entrenamiento.to_dict())
        self._guardar_todos(datos)
        return True

    def obtener_por_id(self, id_entrenamiento: int) -> Optional[Entrenamiento]:
        datos = self._leer_todos()
        for p in datos:
            if p['id'] == id_entrenamiento:
                return Entrenamiento.from_dict(p)
        return None

    def obtener_todos(self) -> List[Entrenamiento]:
        datos = self._leer_todos()
        return [Entrenamiento.from_dict(p) for p in datos]

    def actualizar(self, entrenamiento_actualizado: Entrenamiento) -> bool:
        datos = self._leer_todos()
        for i, p in enumerate(datos):
            if p['id'] == entrenamiento_actualizado.id:
                datos[i] = entrenamiento_actualizado.to_dict()
                self._guardar_todos(datos)
                return True
        return False

    def eliminar(self, id_entrenamiento: int) -> bool:
        datos = self._leer_todos()
        nuevos_datos = [p for p in datos if p['id'] != id_entrenamiento]
        if len(datos) == len(nuevos_datos):
            return False  # No se encontró el entrenamiento
        self._guardar_todos(nuevos_datos)
        return True