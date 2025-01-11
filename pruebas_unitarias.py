import unittest


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def es_mayor(a, b):
    return a > b


class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        # self.assertEqual(a, b)
        self.assertEqual(suma(5, 3), 8)
        # self.assertEqual(suma(5, 3), 9)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)

    def test_es_mayor(self):
        self.assertTrue(es_mayor(5, 3))
        self.assertFalse(es_mayor(3, 5))


unittest.main()

# Evaluaciones más comunes en pruebas unitarias
# assertEqual(a, b): Verifica que a y b sean iguales.
# assertTrue(x): Verifica que x sea verdadero.
# assertFalse(x): Verifica que x sea falso.
# assertRaises(exc, func, *args): Verifica que una función lance una excepción.
