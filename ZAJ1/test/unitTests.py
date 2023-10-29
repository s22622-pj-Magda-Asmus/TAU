import unittest

from ZAJ1.src.Main import *


class TestForCalculator(unittest.TestCase):

    def test_add_simple(self):
        self.assertEqual(8, add(2,6))

    def test_add_negativeValues(self):
        self.assertEqual(-10, add(-4,-6))

    def test_add_mixedValues(self):
        self.assertEqual(-2, add(4,-6))

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