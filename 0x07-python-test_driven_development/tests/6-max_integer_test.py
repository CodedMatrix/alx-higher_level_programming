#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_normal_cases(self):
        """Test normal cases with positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([0, -1, -2]), 0)
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-1]), -1)

    def test_floats(self):
        """Test cases with floats."""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([1.1, 1.2, 1.3]), 1.3)

    def test_strings(self):
        """Test cases with strings, should raise TypeError."""
        with self.assertRaises(TypeError):
            max_integer(["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()
