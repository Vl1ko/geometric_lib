import unittest

import math


def area(r):
    if r >= 0:
      return math.pi * r * r
    else:
      return 0


def perimeter(r):
    if r >= 0:
      return 2 * math.pi * r
    else:
      return 0

class CircleAreaTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

        res = area(-0)
        self.assertEqual(res, 0)

    def test_negative_mul(self):
        res = area(-10)
        self.assertEqual(res, 0)

        res = area(-1)
        self.assertEqual(res, 0)

    def test_natural_mul(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

        res = area(1)
        self.assertEqual(res, 3.141592653589793)


class CirclePerimeterTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

        res = perimeter(-0)
        self.assertEqual(res, 0)

    def test_negative_mul(self):
        res = perimeter(-10)
        self.assertEqual(res, 0)

        res = perimeter(-1)
        self.assertEqual(res, 0)

    def test_natural_mul(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

        res = perimeter(1)
        self.assertEqual(res, 6.283185307179586)
        

