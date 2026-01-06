import unittest
import sut.problem_HumanEval_108 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_array(self):
            """
            Test case: Empty input array.
            Expected: 0, as there are no numbers to count.
            Covers: Edge case (empty collection), return 0.
            """
            self.assertEqual(mod.count_nums([]), 0)

    def test_all_positive_sums(self):
            """
            Test case: Array where all numbers have a sum of digits > 0.
            Expected: 3, as all elements (1, 1, 2) satisfy the condition.
            Covers: Typical input, all elements counted, docstring example.
            """
            self.assertEqual(mod.count_nums([1, 1, 2]), 3)

    def test_mixed_positive_negative_zero_sums(self):
            """
            Test case: Array with positive, negative, and zero-sum numbers.
            -1 (sum -1), 11 (sum 2), -11 (sum 0). Only 11 counts.
            Expected: 1.
            Covers: Typical input, mixed signs, docstring example, logic for negative numbers.
            """
            self.assertEqual(mod.count_nums([-1, 11, -11]), 1)

    def test_single_positive_digit(self):
            """
            Test case: Single element array with a positive single-digit number.
            Expected: 1, as 5 has sum 5 > 0.
            Covers: Edge case (single element), boundary condition (smallest positive sum).
            """
            self.assertEqual(mod.count_nums([5]), 1)

    def test_single_negative_digit(self):
            """
            Test case: Single element array with a negative single-digit number.
            Expected: 0, as -5 has sum -5, which is not > 0.
            Covers: Edge case (single element), boundary condition (negative sum).
            """
            self.assertEqual(mod.count_nums([-5]), 0)

    def test_single_zero_digit(self):
            """
            Test case: Single element array with zero.
            Expected: 0, as 0 has sum 0, which is not > 0.
            Covers: Edge case (single element), boundary condition (sum exactly 0).
            """
            self.assertEqual(mod.count_nums([0]), 0)

    def test_boundary_sum_zero_and_one(self):
            """
            Test case: Numbers whose digit sums are exactly 0 or 1, or slightly negative.
            - 10 (sum 1, count)
            - -11 (sum -1 + 1 = 0, no count)
            - 0 (sum 0, no count)
            - 1 (sum 1, count)
            Expected: 2.
            Covers: Boundary condition (sum > 0 vs sum = 0), off-by-one for the comparison.
            """
            self.assertEqual(mod.count_nums([10, -11, 0, 1]), 2)

    def test_extreme_large_numbers(self):
            """
            Test case: Array with very large positive and negative numbers.
            - 99999 (sum 45, count)
            - -99999 (sum -9 + 9 + 9 + 9 + 9 = 36, count)
            - 100000 (sum 1, count)
            Expected: 3.
            Covers: Extreme/unusual inputs, ensures digit sum logic handles large numbers and negative sign correctly.
            """
            self.assertEqual(mod.count_nums([99999, -99999, 100000]), 3)

    def test_all_negative_sums(self):
            """
            Test case: Array where all numbers result in a sum of digits <= 0.
            - -1 (sum -1)
            - -2 (sum -2)
            - -10 (sum -1)
            - -11 (sum 0)
            - -100 (sum -1)
            Expected: 0.
            Covers: All elements not satisfying condition, ensures counter doesn't increment incorrectly.
            """
            self.assertEqual(mod.count_nums([-1, -2, -10, -11, -100]), 0)

    def test_mixed_digits_negative_numbers(self):
            """
            Test case: Complex negative numbers to verify signed digit rule.
            - -19 (sum -1 + 9 = 8, count)
            - -20 (sum -2 + 0 = -2, no count)
            - -55 (sum -5 + 5 = 0, no count)
            - -101 (sum -1 + 0 + 1 = 0, no count)
            Expected: 1.
            Covers: Logic mutations for negative number digit sum, boundary conditions around 0 for negative numbers.
            """
            self.assertEqual(mod.count_nums([-19, -20, -55, -101]), 1)

    def test_normal_case_all_positive(self):
            arr = [1, 1, 2]
            expected_output = 3
            self.assertEqual(mod.count_nums(arr), expected_output)

    def test_normal_case_mixed_signs(self):
            arr = [-1, 11, -11]
            expected_output = 1
            self.assertEqual(mod.count_nums(arr), expected_output)

    def test_normal_case_with_zero_digit(self):
            arr = [10, -10, 5]
            expected_output = 2
            self.assertEqual(mod.count_nums(arr), expected_output)

    def test_normal_case_multi_digit_numbers(self):
            arr = [123, -45, 6]
            expected_output = 3
            self.assertEqual(mod.count_nums(arr), expected_output)
    
        # Edge Cases

    def test_edge_case_empty_list(self):
            arr = []
            expected_output = 0
            self.assertEqual(mod.count_nums(arr), expected_output)

    def test_edge_case_single_zero(self):
            arr = [0]
            expected_output = 0
            self.assertEqual(mod.count_nums(arr), expected_output)

    def test_edge_case_all_negative_no_match(self):
            arr = [-1, -2, -3]
            expected_output = 0
            self.assertEqual(mod.count_nums(arr), expected_output)

    def test_edge_case_mixed_zero_and_hundreds(self):
            arr = [100, -100, 0]
            expected_output = 1
            self.assertEqual(mod.count_nums(arr), expected_output)

    def test_edge_case_large_positive_number(self):
            arr = [999999999]
            expected_output = 1
            self.assertEqual(mod.count_nums(arr), expected_output)

    def test_edge_case_large_negative_number_with_positive_sum(self):
            # -999999999: sum = -9 + (8 * 9) = -9 + 72 = 63 > 0
            arr = [-999999999]
            expected_output = 1
            self.assertEqual(mod.count_nums(arr), expected_output)
    
        # Error Cases

    def test_error_case_non_integer_element(self):
            arr = [1, 'a', 3]
            with self.assertRaises(TypeError):
                mod.count_nums(arr)

    def test_error_case_input_is_none(self):
            arr = None
            with self.assertRaises(TypeError):
                mod.count_nums(arr)

    def test_error_case_input_is_not_list(self):
            arr = 123
            with self.assertRaises(TypeError):
                mod.count_nums(arr)

