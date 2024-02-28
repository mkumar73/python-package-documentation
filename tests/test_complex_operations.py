import unittest
from fancy_calcy.advanced import ScientificFunctions


class TestScientificFunctions(unittest.TestCase):
    def setUp(self):
        self.sf = ScientificFunctions()

    def test_factorial(self):
        self.assertEqual(self.sf.factorial(5), 120)

    def test_power(self):
        self.assertEqual(self.sf.power(2, 3), 8.0)

    def test_logarithm(self):
        self.assertEqual(self.sf.logarithm(10, 100), 2.0)

    def test_sine(self):
        self.assertAlmostEqual(self.sf.sine(45), 0.7071067811865476)

    def test_cosine(self):
        self.assertAlmostEqual(self.sf.cosine(60), 0.5000000000000001)

    def test_tangent(self):
        self.assertAlmostEqual(self.sf.tangent(30), 0.5773502691896257)

    def test_add_complex(self):
        self.assertEqual(self.sf.add_complex(2+3j, 4+5j), (6+8j))

    def test_subtract_complex(self):
        self.assertEqual(self.sf.subtract_complex(4+5j, 2+3j), (2+2j))


if __name__ == '__main__':
    unittest.main()
