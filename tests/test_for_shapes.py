import unittest
import math

# Определение функции для круга
def area_circle(r):
    if r >= 0:
        return math.pi * r * r
    else:
        return 0

def perimeter_circle(r):
    if r >= 0:
        return 2 * math.pi * r
    else:
        return 0

# Определение функции для квадрата
def area_square(a):
    if a >= 0:
        return a * a
    else:
        return 0

def perimeter_square(a):
    if a >= 0:
        return 4 * a
    else:
        return 0

class CircleAreaTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(area_circle(0), 0)
        self.assertEqual(area_circle(-0), 0)

    def test_negative_area(self):
        self.assertEqual(area_circle(-10), 0)
        self.assertEqual(area_circle(-1), 0)

    def test_natural_area(self):
        self.assertEqual(area_circle(10), 314.1592653589793)
        self.assertEqual(area_circle(1), 3.141592653589793)

class CirclePerimeterTestCase(unittest.TestCase):
    def test_zero_perimeter(self):
        self.assertEqual(perimeter_circle(0), 0)
        self.assertEqual(perimeter_circle(-0), 0)

    def test_negative_perimeter(self):
        self.assertEqual(perimeter_circle(-10), 0)
        self.assertEqual(perimeter_circle(-1), 0)

    def test_natural_perimeter(self):
        self.assertEqual(perimeter_circle(10), 62.83185307179586)
        self.assertEqual(perimeter_circle(1), 6.283185307179586)

class SquareAreaTestCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertEqual(area_square(0), 0)
        self.assertEqual(area_square(-0), 0)

    def test_negative_area(self):
        self.assertEqual(area_square(-10), 0)
        self.assertEqual(area_square(-1), 0)

    def test_natural_area(self):
        self.assertEqual(area_square(10), 100)
        self.assertEqual(area_square(1), 1)

class SquarePerimeterTestCase(unittest.TestCase):
    def test_zero_perimeter(self):
        self.assertEqual(perimeter_square(0), 0)
        self.assertEqual(perimeter_square(-0), 0)

    def test_negative_perimeter(self):
        self.assertEqual(perimeter_square(-10), 0)
        self.assertEqual(perimeter_square(-1), 0)

    def test_natural_perimeter(self):
        self.assertEqual(perimeter_square(10), 4000)
        self.assertEqual(perimeter_square(1), 4)

if __name__ == '__main__':
    unittest.main()