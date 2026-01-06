import unittest
from sut.problem_HumanEval_108 import count_nums

class Test_count_nums(unittest.TestCase):

    # Normal Cases
    def test_normal_case_all_positive(self):
        arr = [1, 1, 2]
        expected_output = 3
        self.assertEqual(count_nums(arr), expected_output)

    def test_normal_case_mixed_signs(self):
        arr = [-1, 11, -11]
        expected_output = 1
        self.assertEqual(count_nums(arr), expected_output)

    def test_normal_case_with_zero_digit(self):
        arr = [10, -10, 5]
        expected_output = 2
        self.assertEqual(count_nums(arr), expected_output)

    def test_normal_case_multi_digit_numbers(self):
        arr = [123, -45, 6]
        expected_output = 3
        self.assertEqual(count_nums(arr), expected_output)

    # Edge Cases
    def test_edge_case_empty_list(self):
        arr = []
        expected_output = 0
        self.assertEqual(count_nums(arr), expected_output)

    def test_edge_case_single_zero(self):
        arr = [0]
        expected_output = 0
        self.assertEqual(count_nums(arr), expected_output)

    def test_edge_case_all_negative_no_match(self):
        arr = [-1, -2, -3]
        expected_output = 0
        self.assertEqual(count_nums(arr), expected_output)

    def test_edge_case_mixed_zero_and_hundreds(self):
        arr = [100, -100, 0]
        expected_output = 1
        self.assertEqual(count_nums(arr), expected_output)

    def test_edge_case_large_positive_number(self):
        arr = [999999999]
        expected_output = 1
        self.assertEqual(count_nums(arr), expected_output)

    def test_edge_case_large_negative_number_with_positive_sum(self):
        # -999999999: sum = -9 + (8 * 9) = -9 + 72 = 63 > 0
        arr = [-999999999]
        expected_output = 1
        self.assertEqual(count_nums(arr), expected_output)

    # Error Cases
    def test_error_case_non_integer_element(self):
        arr = [1, 'a', 3]
        with self.assertRaises(TypeError):
            count_nums(arr)

    def test_error_case_input_is_none(self):
        arr = None
        with self.assertRaises(TypeError):
            count_nums(arr)

    def test_error_case_input_is_not_list(self):
        arr = 123
        with self.assertRaises(TypeError):
            count_nums(arr)