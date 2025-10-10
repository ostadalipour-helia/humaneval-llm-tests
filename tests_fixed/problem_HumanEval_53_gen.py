import unittest
from sut_llm.problem_HumanEval_53 import add

class TestAddFunction(unittest.TestCase):

    def test_positive_integers_from_docstring_1(self):
        """Test with positive integers as per docstring example 1."""
        self.assertEqual(add(2, 3), 5)

    def test_positive_integers_from_docstring_2(self):
        """Test with positive integers as per docstring example 2."""
        self.assertEqual(add(5, 7), 12)

    def test_zero_and_positive(self):
        """Test adding zero to a positive number (boundary case)."""
        self.assertEqual(add(0, 10), 10)

    def test_positive_and_zero(self):
        """Test adding a positive number to zero (boundary case)."""
        self.assertEqual(add(15, 0), 15)

    def test_two_zeros(self):
        """Test adding two zeros (edge case, boundary case)."""
        self.assertEqual(add(0, 0), 0)

    def test_negative_integers(self):
        """Test adding two negative integers (sign testing)."""
        self.assertEqual(add(-5, -3), -8)

    def test_positive_and_negative_sum_positive(self):
        """Test adding a positive and a negative number where sum is positive (sign testing)."""
        self.assertEqual(add(10, -3), 7)

    def test_positive_and_negative_sum_negative(self):
        """Test adding a positive and a negative number where sum is negative (sign testing)."""
        self.assertEqual(add(3, -10), -7)

    def test_positive_and_negative_sum_zero(self):
        """Test adding a positive and a negative number that sum to zero (boundary case)."""
        self.assertEqual(add(7, -7), 0)

    def test_large_positive_integers(self):
        """Test with very large positive integers (extreme input)."""
        self.assertEqual(add(1000000000, 2000000000), 3000000000)