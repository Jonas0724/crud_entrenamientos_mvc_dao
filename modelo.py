class Entrenamiento:
    def __init__(self, id_entrenamiento: int, nombre: str, tipo: str):
        self.id = id_entrenamiento
        self.nombre = nombre
        self.tipo = tipo

    def to_dict(self):
        """Convierte el objeto a diccionario para guardarlo en JSON fácilmente."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo
        }

    @staticmethod
    def from_dict(data: dict):
        """Crea una instancia de Producto a partir de un diccionario."""
        return Entrenamiento(data["id"], data["nombre"], data["tipo"])