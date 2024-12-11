import unittest

def area(a):
  if a >= 0:
    return a * a
  else:
    return 0


def perimeter(a):
  if a >= 0:
    return 4 * a
  else:
    return 0


class SquareAreaTestCase(unittest.TestCase):
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
        self.assertEqual(res, 100)

        res = area(1)
        self.assertEqual(res, 1)


class SquarePerimeterTestCase(unittest.TestCase):
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
        self.assertEqual(res, 40)

        res = perimeter(1)
        self.assertEqual(res, 4)