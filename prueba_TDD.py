import unittest
from Evidencia import MaquinaInyeccionCera  # Importar la clase

class TestMaquinaInyeccionCera(unittest.TestCase):
    
    def setUp(self):
        self.maquina_cera = MaquinaInyeccionCera("Kaya Cast", "2.0", 300)

    def test_cargar_cera(self):
        resultado = self.maquina_cera.cargar_cera(200)
        self.assertEqual(self.maquina_cera.cera_actual, 200)
        self.assertIn("200g de cera cargados", resultado)

        resultado = self.maquina_cera.cargar_cera(200)
        self.assertEqual(self.maquina_cera.cera_actual, 200)
        self.assertIn("No se puede cargar", resultado)

    def test_inyectar_cera(self):
        self.maquina_cera.cargar_cera(300)
        resultado = self.maquina_cera.inyectar_cera(100)
        self.assertEqual(self.maquina_cera.cera_actual, 200)
        self.assertIn("Inyectando 100g de cera", resultado)

        resultado = self.maquina_cera.inyectar_cera(400)
        self.assertEqual(self.maquina_cera.cera_actual, 200)
        self.assertIn("No hay suficiente cera", resultado)

    def test_calentar_cera(self):
        # Probar calentar cera dentro del límite permitido
        resultado = self.maquina_cera.calentar_cera(50)
        self.assertEqual(self.maquina_cera.temperatura, 51)
        self.assertIn("Calentando cera a 50°C", resultado)

        # Probar calentar más allá del límite máximo
        resultado = self.maquina_cera.calentar_cera(50)
        self.assertEqual(self.maquina_cera.temperatura, 100)
        self.assertIn("No se puede calentar más", resultado)

        # Probar un incremento negativo
        resultado = self.maquina_cera.calentar_cera(-10)
        self.assertEqual(self.maquina_cera.temperatura, 100)  # Temperatura no debe cambiar
        self.assertIn("El incremento de la temperatura debe ser positivo", resultado)

if __name__ == '__main__':
    unittest.main()
