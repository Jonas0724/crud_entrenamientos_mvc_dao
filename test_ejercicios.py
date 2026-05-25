import unittest
import os
from controlador import EjercicioControlador
from modelo import Ejercicio
from dao import EjercicioDAO

class TestEjercicioControlador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Se ejecuta una sola vez al inicio de todas las pruebas."""
        cls.archivo_test = "ejercicios_test.json"

    def setUp(self):
        """Se ejecuta ANTES de CADA prueba. Inicializa un entorno limpio."""
        # Forzamos al DAO a usar el archivo de pruebas
        self.controlador = EjercicioControlador()
        self.controlador.dao = EjercicioDAO(archivo_db=self.archivo_test)

    def tearDown(self):
        """Se ejecuta DESPUÉS de CADA prueba. Elimina el archivo temporal."""
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

    # ==========================================
    # 📝 PRUEBAS DE CREACIÓN (CREATE)
    # ==========================================

    def test_1_registrar_ejercicio_exitoso(self):
        """1. Registrar un ejercicio con datos válidos."""
        resultado = self.controlador.registrar_ejercicio(1, "Funcional HIIT", "Cardio")
        self.assertIn("✅", resultado)  # Verifica que devuelva el mensaje de éxito
        
        # Verificar que realmente se guardó en el DAO
        ejercicio = self.controlador.buscar_ejercicios(1)
        self.assertIsNotNone(ejercicio)
        self.assertEqual(ejercicio.nombre, "Funcional HIIT")

    def test_2_registrar_ejercicio_tipo_vacio(self):
        """2. Validar que no permita registrar si el 'tipo' está vacío."""
        resultado = self.controlador.registrar_ejercicio(2, "Spinning", "")
        self.assertIn("❌ Error", resultado)
        
        # Verificar que NO se haya guardado
        ejercicio = self.controlador.buscar_ejercicios(2)
        self.assertIsNone(ejercicio)

    def test_3_registrar_id_duplicado(self):
        """3. Validar que no permita registrar dos ejercicios con el mismo ID."""
        self.controlador.registrar_ejercicio(3, "Yoga", "Flexibilidad")
        # Intentar registrar otro con el mismo ID (3)
        resultado_duplicado = self.controlador.registrar_ejercicio(3, "Pilates", "Fuerza")
        
        self.assertIn("ID del ejercicio ya existe", resultado_duplicado)

    # ==========================================
    # 🔍 PRUEBAS DE LECTURA (READ)
    # ==========================================

    def test_4_buscar_ejercicio_existente(self):
        """4. Buscar un ID que sí existe en el sistema."""
        self.controlador.registrar_ejercicio(4, "Crossfit", "Fuerza")
        ejercicio = self.controlador.buscar_ejercicios(4)
        
        self.assertIsNotNone(ejercicio)
        self.assertEqual(ejercicio.id, 4)

    def test_5_buscar_ejercicio_inexistente(self):
        """5. Buscar un ID que no existe debe retornar None."""
        ejercicio = self.controlador.buscar_ejercicios(999)
        self.assertIsNone(ejercicio)

    def test_6_listar_todos_los_ejercicios(self):
        """6. Listar ejercicios debe devolver la cantidad exacta guardada."""
        self.controlador.registrar_ejercicio(10, "Zumba", "Baile")
        self.controlador.registrar_ejercicio(11, "Boxeo", "Contacto")
        
        lista = self.controlador.listar_ejercicios()
        self.assertEqual(len(lista), 2)

    # ==========================================
    # 🔄 PRUEBAS DE ACTUALIZACIÓN (UPDATE)
    # ==========================================

    def test_7_modificar_ejercicio_exitoso(self):
        """7. Actualizar el nombre y tipo de un ejercicio existente."""
        self.controlador.registrar_ejercicio(7, "Calistenia", "Fuerza")
        
        # Modificamos el ejercicio 7
        resultado = self.controlador.modificar_ejercicio(7, "Calistenia Pro", "Resistencia")
        self.assertIn("✅", resultado)
        
        # Comprobar los cambios
        modificado = self.controlador.buscar_ejercicios(7)
        self.assertEqual(modificado.nombre, "Calistenia Pro")
        self.assertEqual(modificado.tipo, "Resistencia")

    def test_8_modificar_ejercicio_inexistente(self):
        """8. Intentar modificar un ejercicio que no existe en el JSON."""
        resultado = self.controlador.modificar_ejercicio(888, "Fantasma", "Ninguno")
        print(f"\n[DEBUG TEST 8] El controlador respondió: {resultado}") 
        self.assertIn("Ejercicio no encontrado", resultado)

    # ==========================================
    # 🗑️ PRUEBAS DE ELIMINACIÓN (DELETE)
    # ==========================================

    def test_9_borrar_ejercicio_exitoso(self):
        """9. Eliminar un ejercicio existente."""
        self.controlador.registrar_ejercicio(9, "Natación", "Cardio")
        
        resultado = self.controlador.borrar_ejercicio(9)
        self.assertIn("✅", resultado)
        
        # Verificar que ya no existe
        self.assertIsNone(self.controlador.buscar_ejercicios(9))

    def test_10_borrar_ejercicio_inexistente(self):
        """10. Intentar eliminar un ID que no existe."""
        resultado = self.controlador.borrar_ejercicio(999)
        self.assertIn("❌ Error", resultado)


if __name__ == "__main__":
    unittest.main()