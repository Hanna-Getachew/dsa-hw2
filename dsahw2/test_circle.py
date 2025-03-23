import unittest
from calc_app.circle import Circle
import math

class TestCircle(unittest.TestCase):

    def test_perimeter(self):
        c = Circle(5)
        expected = 2 * math.pi * 5
        self.assertAlmostEqual(c.perimeter(), expected, places=5)

    def test_area(self):
        c = Circle(5)
        expected = math.pi * (5 ** 2)
        self.assertAlmostEqual(c.area(), expected, places=5)

if __name__ == '__main__':
    unittest.main()