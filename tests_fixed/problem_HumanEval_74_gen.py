import unittest
from sut_llm.problem_HumanEval_74 import total_match

class TestTotalMatch(unittest.TestCase):

    def test_1_empty_lists(self):
        # Edge Case: Both lists are empty. Total chars are 0 for both.
        # Boundary: Equal counts, should return the first list (which is empty).
        self.assertListEqual(total_match([], []), [])

    def test_2_first_list_has_fewer_chars(self):
        # Boundary: lst1_chars < lst2_chars.
        # Typical Input: lst1 total chars = 7, lst2 total chars = 18.
        self.assertListEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_3_second_list_has_fewer_chars(self):
        # Boundary: lst2_chars < lst1_chars.
        # Typical Input: lst1 total chars = 7, lst2 total chars = 4.
        self.assertListEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])

    def test_4_equal_char_counts_return_first_list(self):
        # Boundary: lst1_chars == lst2_chars.
        # Logic Mutation: Catches if the function incorrectly returns lst2 or a different list on equality.
        # Off-by-one: Simple case with equal small counts.
        self.assertListEqual(total_match(['a', 'b'], ['c', 'd']), ['a', 'b'])

    def test_5_first_list_empty_second_not(self):
        # Edge Case: One list is empty, the other is not.
        # Boundary: lst1_chars < lst2_chars (0 < 3).
        self.assertListEqual(total_match([], ['a', 'b', 'c']), [])

    def test_6_second_list_empty_first_not(self):
        # Edge Case: One list is not empty, the other is empty.
        # Boundary: lst2_chars < lst1_chars (0 < 3).
        self.assertListEqual(total_match(['a', 'b', 'c'], []), [])

    def test_7_single_element_lists_first_smaller(self):
        # Edge Case: Single element lists.
        # Off-by-one: Char counts are 1 vs 2.
        # Boundary: lst1_chars < lst2_chars.
        self.assertListEqual(total_match(['a'], ['b', 'c']), ['a'])

    def test_8_single_element_lists_second_smaller(self):
        # Edge Case: Single element lists.
        # Off-by-one: Char counts are 2 vs 1.
        # Boundary: lst2_chars < lst1_chars.
        self.assertListEqual(total_match(['a', 'b'], ['c']), ['c'])

    def test_9_lists_with_empty_strings_equal_counts(self):
        # Extreme/Unusual Input: Lists containing empty strings.
        # Zero Testing: Ensures empty strings contribute 0 to total char count.
        # Boundary: Equal counts (1 vs 1), should return the first list.
        self.assertListEqual(total_match(['', 'a'], ['', '', 'b']), ['', 'a'])

    def test_10_long_strings_many_elements_second_smaller(self):
        # Extreme/Unusual Input: Lists with longer strings and multiple elements.
        # Boundary: lst2_chars < lst1_chars (39 vs 13).
        self.assertListEqual(total_match(['longstringone', 'longstringtwo', 'longstringthree'], ['short', 'strings']), ['short', 'strings'])