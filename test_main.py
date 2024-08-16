import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(25), 5)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

if __name__ == '__main__':
    unittest.main()

