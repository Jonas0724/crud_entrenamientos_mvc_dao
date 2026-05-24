class Ejercicio:
    def __init__(self, id_ejercicio: int, nombre: str, tipo: str):
        self.id = id_ejercicio
        self.nombre = nombre
        self.tipo = tipo

    def to_dict(self) -> dict:
        """Convierte el objeto a diccionario para guardarlo en JSON."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo
        }

    @staticmethod
    def from_dict(data: dict) -> "Ejercicio":
        """Crea una instancia de Ejercicio desde un diccionario."""
        return Ejercicio(
            data["id"],
            data["nombre"],
            data["tipo"]
        )