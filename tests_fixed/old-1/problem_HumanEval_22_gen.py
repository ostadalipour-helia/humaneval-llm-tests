import unittest
from sut_llm.problem_HumanEval_22 import filter_integers

class TestFilterIntegers(unittest.TestCase):

    def test_docstring_example_1(self):
        """Test case from the docstring: mixed types with one integer."""
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

    def test_docstring_example_2(self):
        """Test case from the docstring: mixed types with multiple integers."""
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

    def test_empty_list(self):
        """Test with an empty input list."""
        self.assertEqual(filter_integers([]), [])

    def test_only_integers(self):
        """Test with a list containing only integers (positive, negative, zero, large)."""
        self.assertEqual(filter_integers([10, -20, 0, 12345678901234567890]), [10, -20, 0, 12345678901234567890])

    def test_no_integers(self):
        """Test with a list containing no integers, only other types."""
        self.assertEqual(filter_integers(['hello', 3.14, None, {}, [], (1,)]), [])

    def test_mixed_types_with_booleans(self):
        """Test with mixed types, specifically including booleans (which are instances of int)."""
        self.assertEqual(filter_integers([True, False, 1, 'test', 0.5]), [True, False, 1])

    def test_only_floats(self):
        """Test with a list containing only floating-point numbers."""
        self.assertEqual(filter_integers([3.14, -2.5, 0.0, 1.0]), [])

    def test_none_and_other_non_integers_with_one_int(self):
        """Test with None, strings, complex objects, and exactly one integer."""
        self.assertEqual(filter_integers([None, '123', {'key': 'value'}, 42, []]), [42])

    def test_list_with_complex_numbers(self):
        """Test with a list containing complex numbers and other non-integers."""
        self.assertEqual(filter_integers([1j, 2+3j, 'complex', 7]), [7])

    def test_list_with_nested_structures(self):
        """Test with a list containing nested lists and dictionaries, ensuring they are not filtered as integers."""
        self.assertEqual(filter_integers([1, [2, 3], {'a': 4}, 5, None]), [1, 5])

if __name__ == '__main__':
    unittest.main()