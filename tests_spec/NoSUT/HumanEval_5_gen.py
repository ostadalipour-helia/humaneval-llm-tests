import unittest
from sut.problem_HumanEval_5 import intersperse

class Test_intersperse(unittest.TestCase):

    def test_normal_case_1(self):
        # Normal case: multiple elements, positive delimeter
        numbers = [1, 2, 3]
        delimeter = 4
        expected_output = [1, 4, 2, 4, 3]
        self.assertEqual(intersperse(numbers, delimeter), expected_output)

    def test_normal_case_2(self):
        # Normal case: multiple elements, zero delimeter
        numbers = [10, 20, 30, 40]
        delimeter = 0
        expected_output = [10, 0, 20, 0, 30, 0, 40]
        self.assertEqual(intersperse(numbers, delimeter), expected_output)

    def test_normal_case_3(self):
        # Normal case: two negative elements, positive delimeter
        numbers = [-1, -2]
        delimeter = 99
        expected_output = [-1, 99, -2]
        self.assertEqual(intersperse(numbers, delimeter), expected_output)

    def test_edge_case_empty_list(self):
        # Edge case: empty numbers list
        numbers = []
        delimeter = 4
        expected_output = []
        self.assertEqual(intersperse(numbers, delimeter), expected_output)

    def test_edge_case_single_element_list(self):
        # Edge case: single element numbers list
        numbers = [1]
        delimeter = 4
        expected_output = [1]
        self.assertEqual(intersperse(numbers, delimeter), expected_output)

    def test_edge_case_single_element_list_negative_delimeter(self):
        # Edge case: single element numbers list with negative delimeter
        numbers = [7]
        delimeter = -1
        expected_output = [7]
        self.assertEqual(intersperse(numbers, delimeter), expected_output)

    def test_error_numbers_is_none(self):
        # Error case: 'numbers' argument is None
        numbers = None
        delimeter = 4
        with self.assertRaises(TypeError):
            intersperse(numbers, delimeter)

    def test_error_numbers_contains_non_integer(self):
        # Error case: 'numbers' list contains non-integer elements
        numbers = [1, "a", 3]
        delimeter = 4
        with self.assertRaises(TypeError):
            intersperse(numbers, delimeter)

    def test_error_delimeter_is_not_integer(self):
        # Error case: 'delimeter' argument is not an integer
        numbers = [1, 2, 3]
        delimeter = "x"
        with self.assertRaises(TypeError):
            intersperse(numbers, delimeter)

    def test_error_numbers_is_not_list(self):
        # Error case: 'numbers' argument is a tuple (not a list)
        numbers = (1, 2, 3)
        delimeter = 4
        with self.assertRaises(TypeError):
            intersperse(numbers, delimeter)

    def test_error_delimeter_is_float(self):
        # Error case: 'delimeter' argument is a float (not an int)
        numbers = [1, 2, 3]
        delimeter = 4.0
        with self.assertRaises(TypeError):
            intersperse(numbers, delimeter)