"""
Sample tests
"""

from django.test import SimpleTestCase
from app import calc

class CaclTests(SimpleTestCase):
    def test_add_numbers(self):
        """
        Adding numbers together
        """
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_number(self):
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)