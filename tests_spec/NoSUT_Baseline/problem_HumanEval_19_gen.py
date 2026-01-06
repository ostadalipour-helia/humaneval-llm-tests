import unittest
import sut.problem_HumanEval_19 as mod

class TestHybrid(unittest.TestCase):
    def test_1_basic_example(self):
            # Test case from the docstring example
            self.assertEqual(mod.sort_numbers('three one five'), 'one three five')

    def test_2_empty_string(self):
            # Edge case: empty input string
            self.assertEqual(mod.sort_numbers(''), '')

    def test_3_single_number(self):
            # Edge case: single number word
            self.assertEqual(mod.sort_numbers('seven'), 'seven')

    def test_4_already_sorted(self):
            # Test case: numbers are already in sorted order
            self.assertEqual(mod.sort_numbers('one two three four'), 'one two three four')

    def test_5_reverse_sorted(self):
            # Test case: numbers are in reverse sorted order
            self.assertEqual(mod.sort_numbers('nine eight seven six'), 'six seven eight nine')

    def test_6_duplicates_and_zero(self):
            # Boundary testing: includes 'zero' (smallest value) and duplicates
            self.assertEqual(mod.sort_numbers('one zero one two'), 'zero one one two')

    def test_7_all_same_numbers(self):
            # Edge case: all numbers are identical
            self.assertEqual(mod.sort_numbers('five five five'), 'five five five')

    def test_8_full_range_unsorted(self):
            # Extreme input: a comprehensive mix of numbers including boundaries 'zero' and 'nine'
            self.assertEqual(mod.sort_numbers('nine zero five two eight one three four seven six'), 'zero one two three four five six seven eight nine')

    def test_9_two_numbers_boundary_check(self):
            # Boundary testing: two numbers, specifically 'zero' and 'one' to catch off-by-one or comparison errors
            self.assertEqual(mod.sort_numbers('one zero'), 'zero one')

    def test_10_mixed_order_with_upper_boundary(self):
            # Boundary testing: numbers near the upper end, mixed order
            self.assertEqual(mod.sort_numbers('eight nine seven'), 'seven eight nine')

    def test_normal_unsorted_numbers(self):
            # Normal case: Typical case with multiple unsorted numbers.
            input_str = "three one five"
            expected_output = "one three five"
            self.assertEqual(mod.sort_numbers(input_str), expected_output)

    def test_normal_already_sorted(self):
            # Normal case: Input is already sorted.
            input_str = "one two three"
            expected_output = "one two three"
            self.assertEqual(mod.sort_numbers(input_str), expected_output)

    def test_normal_duplicate_numbers(self):
            # Normal case: Input with duplicate numbers.
            input_str = "seven four seven one"
            expected_output = "one four seven seven"
            self.assertEqual(mod.sort_numbers(input_str), expected_output)

    def test_normal_all_numbers_reverse(self):
            # Normal case: All numbers in reverse order.
            input_str = "nine eight seven six five four three two one zero"
            expected_output = "zero one two three four five six seven eight nine"
            self.assertEqual(mod.sort_numbers(input_str), expected_output)

    def test_edge_empty_string(self):
            # Edge case: Empty input string.
            input_str = ""
            expected_output = ""
            self.assertEqual(mod.sort_numbers(input_str), expected_output)

    def test_edge_single_number(self):
            # Edge case: Single number in the input string.
            input_str = "five"
            expected_output = "five"
            self.assertEqual(mod.sort_numbers(input_str), expected_output)

    def test_edge_all_identical_numbers(self):
            # Edge case: All numbers are identical.
            input_str = "two two two"
            expected_output = "two two two"
            self.assertEqual(mod.sort_numbers(input_str), expected_output)

    def test_edge_extreme_numbers(self):
            # Edge case: Numbers at the extremes of the valid range.
            input_str = "zero nine"
            expected_output = "zero nine"
            self.assertEqual(mod.sort_numbers(input_str), expected_output)

