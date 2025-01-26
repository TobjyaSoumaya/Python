# tests/test_math_operations.py
import unittest
from src.math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        """Test de la fonction d'addition."""
        self.assertEqual(add(3, 2), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -3), -8)

    def test_subtract(self):
        """Test de la fonction de soustraction."""
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(-1, 1), -2)

    def test_multiply(self):
        """Test de la fonction de multiplication."""
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        """Test de la fonction de division."""
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(9, 3), 3)
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
