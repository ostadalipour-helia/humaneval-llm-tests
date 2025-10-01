import unittest
from sut.problem_HumanEval_74 import total_match

class TestTotalMatch(unittest.TestCase):

    def test_1_empty_lists(self):
        # Test case: Both lists are empty, total chars are 0, should return the first list.
        self.assertEqual(total_match([], []), [])

    def test_2_lst2_has_fewer_chars_example_1(self):
        # Test case from docstring: lst1 (7 chars) vs lst2 (4 chars), should return lst2.
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])

    def test_3_lst1_has_fewer_chars_example_1(self):
        # Test case from docstring: lst1 (7 chars) vs lst2 (16 chars), should return lst1.
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_4_lst2_has_fewer_chars_example_2(self):
        # Test case from docstring: lst1 (7 chars) vs lst2 (6 chars), should return lst2.
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])

    def test_5_lst1_has_fewer_chars_single_vs_multiple(self):
        # Test case from docstring: lst1 (1 char) vs lst2 (5 chars), should return lst1.
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

    def test_6_equal_chars_non_empty_lists(self):
        # Test case: Both lists have non-empty strings and equal total chars (2 vs 2), should return lst1.
        self.assertEqual(total_match(['a', 'b'], ['cc']), ['a', 'b'])

    def test_7_lst1_empty_lst2_not_empty(self):
        # Test case: lst1 is empty (0 chars), lst2 has chars (10 chars), should return lst1.
        self.assertEqual(total_match([], ['hello', 'world']), [])

    def test_8_lst2_empty_lst1_not_empty(self):
        # Test case: lst1 has chars (10 chars), lst2 is empty (0 chars), should return lst2.
        self.assertEqual(total_match(['hello', 'world'], []), [])

    def test_9_lst1_fewer_chars_different_list_lengths(self):
        # Test case: lst1 (3 chars) vs lst2 (4 chars), different number of elements, should return lst1.
        self.assertEqual(total_match(['a', 'b', 'c'], ['dddd']), ['a', 'b', 'c'])

    def test_10_lst2_fewer_chars_different_list_lengths(self):
        # Test case: lst1 (4 chars) vs lst2 (3 chars), different number of elements, should return lst2.
        self.assertEqual(total_match(['dddd'], ['a', 'b', 'c']), ['a', 'b', 'c'])