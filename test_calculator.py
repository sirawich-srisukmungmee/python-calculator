import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 15), 25)

    # Add the following test methods to the TestCalculator class:

# add() (2 test cases)
    def test_add_positive(self):
        self.assertEqual(self.calc.add(8, 12), 20)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-9, 4), -5)

# subtract() (2 test cases)
    def test_subtract_basic(self):
        self.assertEqual(self.calc.subtract(20, 6), 14)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-7, -10), 3)

# multiply() (2 test cases)
    def test_multiply_normal(self):
        self.assertEqual(self.calc.multiply(6, 5), 30)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(8, 0), 0)

# divide() (2 test cases)
    def test_divide_basic(self):
        self.assertEqual(self.calc.divide(36, 4), 9)

    def test_divide_equal(self):
        self.assertEqual(self.calc.divide(20, 20), 1)

# modulo() (2 test cases)
    def test_modulo_basic(self):
        self.assertEqual(self.calc.modulo(22, 7), 1)

    def test_modulo_equal(self):
        self.assertEqual(self.calc.modulo(14, 7), 0)

if __name__ == '__main__':
    unittest.main()

