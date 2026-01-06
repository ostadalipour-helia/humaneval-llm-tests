import unittest
import sut.problem_HumanEval_155 as mod

class TestHybrid(unittest.TestCase):
    def test_1_docstring_example_negative(self):
            # Test a typical negative number from the docstring example
            self.assertEqual(mod.even_odd_count(-12), (1, 1))

    def test_2_docstring_example_positive(self):
            # Test a typical positive number from the docstring example
            self.assertEqual(mod.even_odd_count(123), (1, 2))

    def test_3_zero_input_boundary_edge(self):
            # Test with zero, which is an even digit and an edge case for single-digit numbers
            self.assertEqual(mod.even_odd_count(0), (1, 0))

    def test_4_single_negative_odd_digit_edge(self):
            # Test a single negative odd digit as an edge case
            self.assertEqual(mod.even_odd_count(-5), (0, 1))

    def test_5_all_even_digits_extreme_logic(self):
            # Test a number composed entirely of even digits
            self.assertEqual(mod.even_odd_count(2468), (4, 0))

    def test_6_all_odd_digits_extreme_logic(self):
            # Test a number composed entirely of odd digits
            self.assertEqual(mod.even_odd_count(13579), (0, 5))

    def test_7_number_with_multiple_zeros_boundary(self):
            # Test a number containing multiple zero digits, which are even
            self.assertEqual(mod.even_odd_count(10203), (3, 2))

    def test_8_large_negative_number_sign_extreme(self):
            # Test a large negative number to ensure sign handling and digit counting for many digits
            self.assertEqual(mod.even_odd_count(-987654321), (4, 5))

    def test_9_number_with_duplicate_digits_logic(self):
            # Test a number with duplicate digits to ensure each digit is counted correctly
            self.assertEqual(mod.even_odd_count(112233), (2, 4))

    def test_10_alternating_even_odd_digits_logic_boundary(self):
            # Test a number with alternating even and odd digits
            self.assertEqual(mod.even_odd_count(214365), (3, 3))

    def test_normal_mixed_positive_123(self):
            # Description: Mixed even and odd digits in a positive number.
            num = 123
            expected_output = (1, 2)
            self.assertEqual(mod.even_odd_count(num), expected_output)

    def test_normal_mixed_positive_45678(self):
            # Description: Another positive number with mixed digits.
            num = 45678
            expected_output = (3, 2)
            self.assertEqual(mod.even_odd_count(num), expected_output)

    def test_normal_contains_zero_100(self):
            # Description: Number containing zero digits.
            num = 100
            expected_output = (2, 1)
            self.assertEqual(mod.even_odd_count(num), expected_output)

    def test_edge_negative_number(self):
            # Description: Negative number with mixed digits.
            num = -12
            expected_output = (1, 1)
            self.assertEqual(mod.even_odd_count(num), expected_output)

    def test_edge_zero_input(self):
            # Description: Input is zero (0 is an even digit).
            num = 0
            expected_output = (1, 0)
            self.assertEqual(mod.even_odd_count(num), expected_output)

    def test_edge_single_odd_digit(self):
            # Description: Single odd digit number.
            num = 5
            expected_output = (0, 1)
            self.assertEqual(mod.even_odd_count(num), expected_output)

    def test_edge_all_even_digits(self):
            # Description: All even digits.
            num = 246
            expected_output = (3, 0)
            self.assertEqual(mod.even_odd_count(num), expected_output)

    def test_edge_all_odd_digits(self):
            # Description: All odd digits.
            num = 135
            expected_output = (0, 3)
            self.assertEqual(mod.even_odd_count(num), expected_output)

    def test_edge_large_negative_number(self):
            # Description: Large negative number with mixed digits.
            num = -987654321
            expected_output = (4, 5)
            self.assertEqual(mod.even_odd_count(num), expected_output)

    def test_error_string_input(self):
            # Description: Input is a string instead of an integer.
            num = "123"
            with self.assertRaises(TypeError):
                mod.even_odd_count(num)

    def test_error_list_input(self):
            # Description: Input is a list instead of an integer.
            num = [1, 2, 3]
            with self.assertRaises(TypeError):
                mod.even_odd_count(num)

