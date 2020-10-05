"""Test out classify triangle module"""
import unittest

from HW1.Classify_Triangle import classify_triangle


class Test(unittest.TestCase):
    """Test cases"""

    def test_int_a(self):
        """Test if a is a string """
        self.assertEqual(classify_triangle("a", 2, 7), "Invalid input")

    def test_int_b(self):
        """Test if b is not an int"""
        self.assertEqual(classify_triangle(8, "2", 7), "Invalid input")

    def test_int_c(self):
        """Test if c is not an int"""
        self.assertEqual(classify_triangle(8, 4, 3.2), "Invalid input")

    def test_a_too_large(self):
        """Tests if a is larger than b and c"""
        self.assertEqual(classify_triangle(19, 7, 5), "Not a triangle")

    def test_b_too_large(self):
        """Tests if b is larger than a and c"""
        self.assertEqual(classify_triangle(3, 8, 5), "Not a triangle")

    def test_c_too_large(self):
        """Tests if c is larger than b and a"""
        self.assertEqual(classify_triangle(19, 7,59), "Not a triangle")

    def test_a_too_small(self):
        """Tests if a is 0 or smaller"""
        self.assertEqual(classify_triangle(-4, 6, 3), "Not a triangle")

    def test_b_too_small(self):
        """Tests if b is 0 or smaller"""
        self.assertEqual(classify_triangle(4, -6, 3), "Not a triangle")

    def test_c_too_small(self):
        """Tests if c is 0 or smaller"""
        self.assertEqual(classify_triangle(4, 4, 0), "Not a triangle")

    def test_equilateral(self):
        """Tests an equilateral triangle"""
        self.assertEqual(classify_triangle(1,1,1), "Equilateral")

    def test_iso(self):
        """Tests an iso triangle"""
        self.assertEqual(classify_triangle(3,2,2), "Isosceles")

    def test_iso_front_two(self):
        """Tests an iso triangle"""
        self.assertEqual(classify_triangle(7,7,4), "Isosceles")

    def test_iso_edges(self):
        """Tests an iso triangle"""
        self.assertEqual(classify_triangle(5,2,5), "Isosceles")

    def test_scaline_not_right(self):
        """Tests a scaline triangle that is not right"""
        self.assertEqual(classify_triangle(4,2,3), "Scalene")

    def test_scaline_right(self):
        """Tests a right triangle that is right"""
        self.assertEqual(classify_triangle(5,4,3), "Right Scalene")

    def test_right_middle_num_is_largest(self):
        """Tests a right triangle that is right"""
        self.assertEqual(classify_triangle(3,5,4), "Right Scalene")

    def test_right_last_num_is_largest(self):
        """Tests a right triangle that is right"""
        self.assertEqual(classify_triangle(3,4,5), "Right Scalene")
if __name__ == '__main__':
    unittest.main()
