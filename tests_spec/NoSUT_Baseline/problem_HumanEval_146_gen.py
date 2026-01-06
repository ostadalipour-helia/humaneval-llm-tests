import unittest
import sut.problem_HumanEval_146 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_list(self):
            # Edge Case: Test with an empty list.
            # Expected: 0 elements satisfy the conditions.
            self.assertEqual(mod.specialFilter([]), 0)

    def test_docstring_example_1(self):
            # Typical Input: Test with the first example from the docstring.
            # [15, -73, 14, -15]
            # 15: >10, first digit 1 (odd), last digit 5 (odd) -> COUNT
            # -73: not >10
            # 14: >10, first digit 1 (odd), last digit 4 (even) -> NO COUNT
            # -15: not >10
            # Expected: 1
            self.assertEqual(mod.specialFilter([15, -73, 14, -15]), 1)

    def test_docstring_example_2(self):
            # Typical Input: Test with the second example from the docstring.
            # [33, -2, -3, 45, 21, 109]
            # 33: >10, first digit 3 (odd), last digit 3 (odd) -> COUNT
            # -2: not >10
            # -3: not >10
            # 45: >10, first digit 4 (even) -> NO COUNT
            # 21: >10, first digit 2 (even) -> NO COUNT
            # 109: >10, first digit 1 (odd), last digit 9 (odd) -> COUNT
            # Expected: 2
            self.assertEqual(mod.specialFilter([33, -2, -3, 45, 21, 109]), 2)

    def test_boundary_around_ten(self):
            # Boundary Testing: Numbers exactly 10, just below 10, and just above 10.
            # 9: not >10
            # 10: not >10
            # 11: >10, first 1 (odd), last 1 (odd) -> COUNT
            # 13: >10, first 1 (odd), last 3 (odd) -> COUNT
            # Expected: 2
            self.assertEqual(mod.specialFilter([9, 10, 11, 13]), 2)

    def test_logic_mutation_first_odd_last_even(self):
            # Logic Mutation: Test cases where first digit is odd but last digit is even.
            # This should not be counted, catching 'and' vs 'or' errors.
            # 12: >10, first 1 (odd), last 2 (even) -> NO COUNT
            # 14: >10, first 1 (odd), last 4 (even) -> NO COUNT
            # 16: >10, first 1 (odd), last 6 (even) -> NO COUNT
            # 18: >10, first 1 (odd), last 8 (even) -> NO COUNT
            # Expected: 0
            self.assertEqual(mod.specialFilter([12, 14, 16, 18]), 0)

    def test_logic_mutation_first_even_last_odd(self):
            # Logic Mutation: Test cases where first digit is even but last digit is odd.
            # This should not be counted, catching 'and' vs 'or' errors.
            # 21: >10, first 2 (even) -> NO COUNT
            # 43: >10, first 4 (even) -> NO COUNT
            # 65: >10, first 6 (even) -> NO COUNT
            # 87: >10, first 8 (even) -> NO COUNT
            # Expected: 0
            self.assertEqual(mod.specialFilter([21, 43, 65, 87]), 0)

    def test_negative_numbers_and_zero(self):
            # Extreme/Unusual Input: Test with negative numbers and zero.
            # -11: not >10
            # -15: not >10
            # 0: not >10
            # 10: not >10
            # 11: >10, first 1 (odd), last 1 (odd) -> COUNT
            # Expected: 1
            self.assertEqual(mod.specialFilter([-11, -15, 0, 10, 11]), 1)

    def test_single_element_list(self):
            # Edge Case: Test with a single element list.
            # 15: >10, first 1 (odd), last 5 (odd) -> COUNT
            # Expected: 1
            self.assertEqual(mod.specialFilter([15]), 1)

    def test_all_elements_satisfy_conditions(self):
            # Extreme/Unusual Input: All elements in the list satisfy the conditions.
            # 11: COUNT
            # 13: COUNT
            # 15: COUNT
            # 17: COUNT
            # 19: COUNT
            # 31: COUNT
            # 33: COUNT
            # Expected: 7
            self.assertEqual(mod.specialFilter([11, 13, 15, 17, 19, 31, 33]), 7)

    def test_large_numbers_and_zeros_in_digits(self):
            # Extreme/Unusual Input & Boundary: Test with large numbers and numbers containing zero digits.
            # 101: >10, first 1 (odd), last 1 (odd) -> COUNT
            # 109: >10, first 1 (odd), last 9 (odd) -> COUNT
            # 110: >10, first 1 (odd), last 0 (even) -> NO COUNT
            # 130: >10, first 1 (odd), last 0 (even) -> NO COUNT
            # 13579: >10, first 1 (odd), last 9 (odd) -> COUNT
            # Expected: 3
            self.assertEqual(mod.specialFilter([101, 109, 110, 130, 13579]), 3)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_example_one(self):
            # Example from docstring: 15 matches (15 > 10, first digit 1 odd, last digit 5 odd).
            # Other numbers do not meet the criteria.
            nums = [15, -73, 14, -15]
            expected_output = 1
            self.assertEqual(mod.specialFilter(nums), expected_output)

    def test_normal_example_two(self):
            # Example from docstring: 33 matches (33 > 10, first digit 3 odd, last digit 3 odd).
            # 109 matches (109 > 10, first digit 1 odd, last digit 9 odd).
            # Other numbers do not meet the criteria.
            nums = [33, -2, -3, 45, 21, 109]
            expected_output = 2
            self.assertEqual(mod.specialFilter(nums), expected_output)

    def test_normal_all_match(self):
            # All numbers in the list are greater than 10 and have both first and last digits odd.
            nums = [11, 13, 15, 17, 19]
            expected_output = 5
            self.assertEqual(mod.specialFilter(nums), expected_output)

    def test_normal_large_numbers(self):
            # Large numbers where both first and last digits are odd and are greater than 10.
            nums = [123456789, 987654321]
            expected_output = 2
            self.assertEqual(mod.specialFilter(nums), expected_output)

    def test_edge_empty_list(self):
            # An empty list should result in 0 matching elements.
            nums = []
            expected_output = 0
            self.assertEqual(mod.specialFilter(nums), expected_output)

    def test_edge_no_matches(self):
            # List with no matching elements (either not greater than 10 or digits are not both odd).
            nums = [10, 20, 30, 40, 1, 9, 0, -100]
            expected_output = 0
            self.assertEqual(mod.specialFilter(nums), expected_output)

    def test_edge_greater_than_10_but_digits_not_odd(self):
            # Numbers greater than 10 but with at least one even digit (first or last).
            nums = [12, 14, 16, 21, 43, 65]
            expected_output = 0
            self.assertEqual(mod.specialFilter(nums), expected_output)

    def test_edge_middle_digits_can_be_even_or_zero(self):
            # Numbers with first and last digits odd, but middle digits can be even/zero.
            nums = [101, 103, 105, 107, 109]
            expected_output = 5
            self.assertEqual(mod.specialFilter(nums), expected_output)

    def test_error_input_not_a_list(self):
            # Raise a TypeError because the input is not a list.
            nums = "not_a_list"
            with self.assertRaises(TypeError):
                mod.specialFilter(nums)

    def test_error_list_contains_non_integer_string(self):
            # Raise a TypeError because the list contains non-integer elements.
            nums = [1, 2, "three", 4]
            with self.assertRaises(TypeError):
                mod.specialFilter(nums)

    def test_error_list_contains_non_integer_none(self):
            # Raise a TypeError because the list contains non-integer elements (null in JSON is None in Python).
            nums = [1, 2, None, 4]
            with self.assertRaises(TypeError):
                mod.specialFilter(nums)

