import unittest
import sut.problem_HumanEval_5 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_list(self):
            """
            Test case: Empty input list.
            Boundary condition: Smallest possible list.
            Expected: An empty list.
            """
            self.assertListEqual(mod.intersperse([], 4), [])

    def test_single_element_list(self):
            """
            Test case: Single element input list.
            Boundary condition: List with one element.
            Expected: The original list, as no elements to intersperse between.
            """
            self.assertListEqual(mod.intersperse([1], 4), [1])

    def test_two_elements_list(self):
            """
            Test case: Two element input list.
            Boundary condition: Smallest list where intersperse should add one delimiter.
            Expected: List with one delimiter inserted.
            """
            self.assertListEqual(mod.intersperse([1, 2], 4), [1, 4, 2])

    def test_typical_three_elements(self):
            """
            Test case: Typical three element input list.
            Expected: List with two delimiters inserted. (From docstring)
            """
            self.assertListEqual(mod.intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_longer_list_positive_delimiter(self):
            """
            Test case: A longer list with a positive delimiter.
            Typical/Extreme input: Verifies correct behavior for more elements.
            """
            self.assertListEqual(mod.intersperse([10, 20, 30, 40, 50], 5), [10, 5, 20, 5, 30, 5, 40, 5, 50])

    def test_list_with_zero_delimiter(self):
            """
            Test case: Input list with a zero as the delimiter.
            Sign/Zero testing: Checks handling of zero delimiter.
            """
            self.assertListEqual(mod.intersperse([1, 2, 3], 0), [1, 0, 2, 0, 3])

    def test_list_with_negative_delimiter(self):
            """
            Test case: Input list with a negative delimiter.
            Sign/Zero testing: Checks handling of negative delimiter.
            """
            self.assertListEqual(mod.intersperse([1, 2, 3], -5), [1, -5, 2, -5, 3])

    def test_list_with_negative_numbers(self):
            """
            Test case: Input list containing negative numbers.
            Sign/Zero testing: Checks handling of negative numbers in the input list.
            """
            self.assertListEqual(mod.intersperse([-1, -2, -3], 4), [-1, 4, -2, 4, -3])

    def test_list_with_zero_and_duplicates(self):
            """
            Test case: Input list containing zeros and duplicate numbers.
            Edge case: Checks handling of non-unique and zero values in the list.
            """
            self.assertListEqual(mod.intersperse([0, 0, 5, 5], 1), [0, 1, 0, 1, 5, 1, 5])

    def test_list_all_same_values(self):
            """
            Test case: Input list where all elements are the same.
            Edge case: Ensures logic doesn't depend on unique values.
            """
            self.assertListEqual(mod.intersperse([7, 7, 7, 7], 9), [7, 9, 7, 9, 7, 9, 7])

    def test_normal_case_1(self):
            # Normal case: multiple elements, positive delimeter
            numbers = [1, 2, 3]
            delimeter = 4
            expected_output = [1, 4, 2, 4, 3]
            self.assertEqual(mod.intersperse(numbers, delimeter), expected_output)

    def test_normal_case_2(self):
            # Normal case: multiple elements, zero delimeter
            numbers = [10, 20, 30, 40]
            delimeter = 0
            expected_output = [10, 0, 20, 0, 30, 0, 40]
            self.assertEqual(mod.intersperse(numbers, delimeter), expected_output)

    def test_normal_case_3(self):
            # Normal case: two negative elements, positive delimeter
            numbers = [-1, -2]
            delimeter = 99
            expected_output = [-1, 99, -2]
            self.assertEqual(mod.intersperse(numbers, delimeter), expected_output)

    def test_edge_case_empty_list(self):
            # Edge case: empty numbers list
            numbers = []
            delimeter = 4
            expected_output = []
            self.assertEqual(mod.intersperse(numbers, delimeter), expected_output)

    def test_edge_case_single_element_list(self):
            # Edge case: single element numbers list
            numbers = [1]
            delimeter = 4
            expected_output = [1]
            self.assertEqual(mod.intersperse(numbers, delimeter), expected_output)

    def test_edge_case_single_element_list_negative_delimeter(self):
            # Edge case: single element numbers list with negative delimeter
            numbers = [7]
            delimeter = -1
            expected_output = [7]
            self.assertEqual(mod.intersperse(numbers, delimeter), expected_output)

