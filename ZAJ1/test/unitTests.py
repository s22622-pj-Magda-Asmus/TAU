import unittest

from ZAJ1.src.Main import *


class TestForCalculator(unittest.TestCase):

    # add() function
    def test_add_simple(self):
        self.assertEqual(8, add(2,6))

    def test_add_negativeValues(self):
        self.assertEqual(-10, add(-4,-6))

    def test_add_mixedValues(self):
        self.assertEqual(-2, add(4,-6))

    def test_add_zero(self):
        self.assertEqual(4, add(4,0))

    # subtract() function

    def test_minus_simple(self):
        result = subtract(10, 10)
        self.assertEqual(result, 0)

    def test_minus_positive_value(self):
        result = subtract(10, 8)
        self.assertLess(result, 10)

    def test_minus_negative_value(self):
        result = subtract(10, -8)
        self.assertGreater(result, 10)


    # divide() function
    def test_divide_numbers(self):
        result = divide(10, 3)
        self.assertAlmostEqual(3.333 ,result, places=2)

    def test_divide_byNegativeNumbers(self):
        result = divide(7, -3)
        self.assertAlmostEqual(-2.33, result, places=2)

    def test_divide_by_zero(self):
        result = divide(10, 0)
        self.assertIsInstance(result, ZeroDivisionError)

if __name__ == '__main__':
    unittest.main()