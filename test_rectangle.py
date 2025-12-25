

import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(area(5, 3), 15)

    def test_area_square(self):
        self.assertEqual(area(4, 4), 16)

    def test_area_zero(self):
        self.assertEqual(area(0, 10), 0)

    def test_area_zero_both(self):
        self.assertEqual(area(0, 0), 0)

    def test_area_large_numbers(self):
        self.assertEqual(area(1000, 2000), 2_000_000)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(5, 3), 16)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(4, 4), 16)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 10), 20)

    def test_perimeter_zero_both(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_large_numbers(self):
        self.assertEqual(perimeter(1000, 2000), 6000)
