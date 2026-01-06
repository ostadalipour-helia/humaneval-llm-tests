import unittest
from sut.problem_HumanEval_22 import filter_integers

class Test_filter_integers(unittest.TestCase):

    def test_normal_mixed_string_float_int(self):
        # Description: Mixed list with strings, floats, and integers.
        values = ['a', 3.14, 5]
        expected_output = [5]
        self.assertEqual(filter_integers(values), expected_output)

    def test_normal_mixed_types(self):
        # Description: Mixed list with integers, strings, dictionaries, and lists.
        values = [1, 2, 3, 'abc', {}, []]
        expected_output = [1, 2, 3]
        self.assertEqual(filter_integers(values), expected_output)

    def test_normal_mixed_string_float_int_2(self):
        # Description: Mixed list with integers, strings, and floats.
        values = [10, 'hello', 20, 30.5, 40]
        expected_output = [10, 20, 40]
        self.assertEqual(filter_integers(values), expected_output)

    def test_edge_empty_list(self):
        # Description: An empty input list.
        values = []
        expected_output = []
        self.assertEqual(filter_integers(values), expected_output)

    def test_edge_no_integers(self):
        # Description: A list containing no integers.
        values = ['a', 3.14, 'b', None]
        expected_output = []
        self.assertEqual(filter_integers(values), expected_output)

    def test_edge_only_integers(self):
        # Description: A list containing only integers.
        values = [1, 2, 3, 4]
        expected_output = [1, 2, 3, 4]
        self.assertEqual(filter_integers(values), expected_output)

    def test_edge_booleans_and_integers(self):
        # Description: A list containing booleans (which are subclasses of int) and an integer.
        values = [True, False, 10]
        expected_output = [True, False, 10] # Booleans are instances of int
        self.assertEqual(filter_integers(values), expected_output)

    def test_edge_zero_negative_integers(self):
        # Description: A list containing zero and negative integers.
        values = [0, -5, 100]
        expected_output = [0, -5, 100]
        self.assertEqual(filter_integers(values), expected_output)

    def test_error_none_input(self):
        # Description: Input 'values' is not a list (e.g., None).
        with self.assertRaises(TypeError):
            filter_integers(None)

    def test_error_string_input(self):
        # Description: Input 'values' is not a list (e.g., a string).
        with self.assertRaises(TypeError):
            filter_integers("not a list")

    def test_error_int_input(self):
        # Description: Input 'values' is not a list (e.g., an integer).
        with self.assertRaises(TypeError):
            filter_integers(123)