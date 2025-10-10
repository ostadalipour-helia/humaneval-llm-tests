import unittest
from sut_llm.problem_HumanEval_155 import even_odd_count

class TestEvenOddCount(unittest.TestCase):

    def test_1_docstring_example_negative(self):
        # Test a typical negative number from the docstring example
        self.assertEqual(even_odd_count(-12), (1, 1))

    def test_2_docstring_example_positive(self):
        # Test a typical positive number from the docstring example
        self.assertEqual(even_odd_count(123), (1, 2))

    def test_3_zero_input_boundary_edge(self):
        # Test with zero, which is an even digit and an edge case for single-digit numbers
        self.assertEqual(even_odd_count(0), (1, 0))

    def test_4_single_negative_odd_digit_edge(self):
        # Test a single negative odd digit as an edge case
        self.assertEqual(even_odd_count(-5), (0, 1))

    def test_5_all_even_digits_extreme_logic(self):
        # Test a number composed entirely of even digits
        self.assertEqual(even_odd_count(2468), (4, 0))

    def test_6_all_odd_digits_extreme_logic(self):
        # Test a number composed entirely of odd digits
        self.assertEqual(even_odd_count(13579), (0, 5))

    def test_7_number_with_multiple_zeros_boundary(self):
        # Test a number containing multiple zero digits, which are even
        self.assertEqual(even_odd_count(10203), (3, 2))

    def test_8_large_negative_number_sign_extreme(self):
        # Test a large negative number to ensure sign handling and digit counting for many digits
        self.assertEqual(even_odd_count(-987654321), (4, 5))

    def test_9_number_with_duplicate_digits_logic(self):
        # Test a number with duplicate digits to ensure each digit is counted correctly
        self.assertEqual(even_odd_count(112233), (2, 4))

    def test_10_alternating_even_odd_digits_logic_boundary(self):
        # Test a number with alternating even and odd digits
        self.assertEqual(even_odd_count(214365), (3, 3))