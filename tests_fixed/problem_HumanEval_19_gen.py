import unittest
from sut_llm.problem_HumanEval_19 import sort_numbers


class TestSortNumbers(unittest.TestCase):

    def test_1_basic_example(self):
        # Test case from the docstring example
        self.assertEqual(sort_numbers('three one five'), 'one three five')

    def test_2_empty_string(self):
        # Edge case: empty input string
        self.assertEqual(sort_numbers(''), '')

    def test_3_single_number(self):
        # Edge case: single number word
        self.assertEqual(sort_numbers('seven'), 'seven')

    def test_4_already_sorted(self):
        # Test case: numbers are already in sorted order
        self.assertEqual(sort_numbers('one two three four'), 'one two three four')

    def test_5_reverse_sorted(self):
        # Test case: numbers are in reverse sorted order
        self.assertEqual(sort_numbers('nine eight seven six'), 'six seven eight nine')

    def test_6_duplicates_and_zero(self):
        # Boundary testing: includes 'zero' (smallest value) and duplicates
        self.assertEqual(sort_numbers('one zero one two'), 'zero one one two')

    def test_7_all_same_numbers(self):
        # Edge case: all numbers are identical
        self.assertEqual(sort_numbers('five five five'), 'five five five')

    def test_8_full_range_unsorted(self):
        # Extreme input: a comprehensive mix of numbers including boundaries 'zero' and 'nine'
        self.assertEqual(sort_numbers('nine zero five two eight one three four seven six'), 'zero one two three four five six seven eight nine')

    def test_9_two_numbers_boundary_check(self):
        # Boundary testing: two numbers, specifically 'zero' and 'one' to catch off-by-one or comparison errors
        self.assertEqual(sort_numbers('one zero'), 'zero one')

    def test_10_mixed_order_with_upper_boundary(self):
        # Boundary testing: numbers near the upper end, mixed order
        self.assertEqual(sort_numbers('eight nine seven'), 'seven eight nine')