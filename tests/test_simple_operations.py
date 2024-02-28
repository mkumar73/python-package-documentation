from fancy_calcy.basics import BasicOperations
import unittest


class TestBasicOperations(unittest.TestCase):
    def test_add(self):
        calc = BasicOperations(5, 3)
        result = calc.add()
        self.assertEqual(result, 8)

    def test_subtract(self):
        calc = BasicOperations(5, 3)
        result = calc.subtract()
        self.assertEqual(result, 2)

    def test_multiply(self):
        calc = BasicOperations(5, 3)
        result = calc.multiply()
        self.assertEqual(result, 15)

    def test_divide(self):
        calc = BasicOperations(5, 3)
        result = calc.divide()
        self.assertAlmostEqual(result, 1.6666666666666667)

    def test_integer_divide(self):
        calc = BasicOperations(5, 3)
        result = calc.integer_divide()
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
