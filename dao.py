import json
import os
from typing import List, Optional

from modelo import Ejercicio


class EjercicioDAO:

    def __init__(self, archivo_db="ejercicios.json"):
        self.archivo_db = archivo_db
        self._inicializar_bd()

    def _inicializar_bd(self):
        """Crea el archivo JSON si no existe."""
        if not os.path.exists(self.archivo_db):
            with open(self.archivo_db, 'w', encoding='utf-8') as archivo:
                json.dump([], archivo)

    def _leer_todos(self) -> List[dict]:
        """Lee todos los ejercicios almacenados."""
        with open(self.archivo_db, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)

    def _guardar_todos(self, datos: List[dict]):
        """Guarda todos los ejercicios en el archivo."""
        with open(self.archivo_db, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4)

    # === OPERACIONES CRUD ===

    def crear(self, ejercicio: Ejercicio) -> bool:
        datos = self._leer_todos()

        # Verificar que el ID no exista
        if any(e['id'] == ejercicio.id for e in datos):
            return False

        datos.append(ejercicio.to_dict())
        self._guardar_todos(datos)

        return True

    def obtener_por_id(self, id_ejercicio: int) -> Optional[Ejercicio]:
        datos = self._leer_todos()

        for ejercicio in datos:
            if ejercicio['id'] == id_ejercicio:
                return Ejercicio.from_dict(ejercicio)

        return None

    def obtener_todos(self) -> List[Ejercicio]:
        datos = self._leer_todos()

        return [Ejercicio.from_dict(e) for e in datos]

    def actualizar(self, ejercicio_actualizado: Ejercicio) -> bool:
        datos = self._leer_todos()

        for indice, ejercicio in enumerate(datos):
            if ejercicio['id'] == ejercicio_actualizado.id:
                datos[indice] = ejercicio_actualizado.to_dict()
                self._guardar_todos(datos)

                return True

        return False

    def eliminar(self, id_ejercicio: int) -> bool:
        datos = self._leer_todos()

        nuevos_datos = [
            ejercicio for ejercicio in datos
            if ejercicio['id'] != id_ejercicio
        ]

        if len(datos) == len(nuevos_datos):
            return False

        self._guardar_todos(nuevos_datos)

        return True