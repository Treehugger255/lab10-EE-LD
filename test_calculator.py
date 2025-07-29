# https://github.com/Treehugger255/lab10-EE-LD
# Partner 1: Ethan Eschrich
# Partner 2: Luke Dunham
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(36, 0), 36)
        self.assertEqual(add(10, 11), 21)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(11, 11), 0)
        self.assertEqual(subtract(37, 2), 35)
        self.assertEqual(subtract(33, 21), 12)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(-5, -5), 25) # Negative + Negative
        self.assertEqual(mul(7, -3), -21) # Positive + Negative
        self.assertEqual(mul(6, 8), 48) # Positive + Positive
        self.assertEqual(mul(0, 0), 0) # 0

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(2, 5), 2.5)
        self.assertAlmostEqual(div(5, -2), -0.4)
        self.assertAlmostEqual(div(-2, -2), 1.0)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(5, 1), 0)
        self.assertEqual(logarithm(7, 7), 1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, 0)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(1,1), 2 ** 0.5)
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, -12), 13)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
               square_root(-1)

        self.assertAlmostEqual(square_root(4), 2.0)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)
        self.assertAlmostEqual(square_root(0), 0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
