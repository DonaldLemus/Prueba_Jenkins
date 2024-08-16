# test_main.py

import unittest
from main import suma

class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(3, 5), 8)

    def test_suma_negativos(self):
        self.assertEqual(suma(-3, -5), -8)

    def test_suma_cero(self):
        self.assertEqual(suma(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
