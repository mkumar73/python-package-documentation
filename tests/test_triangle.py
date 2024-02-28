import unittest
from fancy_calcy.triangle import calculate_hypotenuse


class TestTriangle(unittest.TestCase):
    def test_calculate_hypotenuse(self):
        # Test with positive base and height
        self.assertAlmostEqual(calculate_hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculate_hypotenuse(5, 12), 13.0)

        # Test with base and height equal to zero
        with self.assertRaises(ValueError):
            calculate_hypotenuse(0, 4)
        with self.assertRaises(ValueError):
            calculate_hypotenuse(5, 0)

        # Test with negative base and height
        with self.assertRaises(ValueError):
            calculate_hypotenuse(-3, 4)
        with self.assertRaises(ValueError):
            calculate_hypotenuse(5, -12)


if __name__ == '__main__':
    unittest.main()
