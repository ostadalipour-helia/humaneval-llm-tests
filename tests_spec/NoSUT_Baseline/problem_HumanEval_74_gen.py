import unittest
import sut.problem_HumanEval_74 as mod

class TestHybrid(unittest.TestCase):
    def test_1_empty_lists(self):
            # Edge Case: Both lists are empty. Total chars are 0 for both.
            # Boundary: Equal counts, should return the first list (which is empty).
            self.assertListEqual(mod.total_match([], []), [])

    def test_2_first_list_has_fewer_chars(self):
            # Boundary: lst1_chars < lst2_chars.
            # Typical Input: lst1 total chars = 7, lst2 total chars = 18.
            self.assertListEqual(mod.total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])

    def test_3_second_list_has_fewer_chars(self):
            # Boundary: lst2_chars < lst1_chars.
            # Typical Input: lst1 total chars = 7, lst2 total chars = 4.
            self.assertListEqual(mod.total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])

    def test_4_equal_char_counts_return_first_list(self):
            # Boundary: lst1_chars == lst2_chars.
            # Logic Mutation: Catches if the function incorrectly returns lst2 or a different list on equality.
            # Off-by-one: Simple case with equal small counts.
            self.assertListEqual(mod.total_match(['a', 'b'], ['c', 'd']), ['a', 'b'])

    def test_5_first_list_empty_second_not(self):
            # Edge Case: One list is empty, the other is not.
            # Boundary: lst1_chars < lst2_chars (0 < 3).
            self.assertListEqual(mod.total_match([], ['a', 'b', 'c']), [])

    def test_6_second_list_empty_first_not(self):
            # Edge Case: One list is not empty, the other is empty.
            # Boundary: lst2_chars < lst1_chars (0 < 3).
            self.assertListEqual(mod.total_match(['a', 'b', 'c'], []), [])

    def test_7_single_element_lists_first_smaller(self):
            # Edge Case: Single element lists.
            # Off-by-one: Char counts are 1 vs 2.
            # Boundary: lst1_chars < lst2_chars.
            self.assertListEqual(mod.total_match(['a'], ['b', 'c']), ['a'])

    def test_8_single_element_lists_second_smaller(self):
            # Edge Case: Single element lists.
            # Off-by-one: Char counts are 2 vs 1.
            # Boundary: lst2_chars < lst1_chars.
            self.assertListEqual(mod.total_match(['a', 'b'], ['c']), ['c'])

    def test_9_lists_with_empty_strings_equal_counts(self):
            # Extreme/Unusual Input: Lists containing empty strings.
            # Zero Testing: Ensures empty strings contribute 0 to total char count.
            # Boundary: Equal counts (1 vs 1), should return the first list.
            self.assertListEqual(mod.total_match(['', 'a'], ['', '', 'b']), ['', 'a'])

    def test_10_long_strings_many_elements_second_smaller(self):
            # Extreme/Unusual Input: Lists with longer strings and multiple elements.
            # Boundary: lst2_chars < lst1_chars (39 vs 13).
            self.assertListEqual(mod.total_match(['longstringone', 'longstringtwo', 'longstringthree'], ['short', 'strings']), ['short', 'strings'])

    def test_normal_case_1_lst2_shorter(self):
            lst1 = ["hi", "admin"]
            lst2 = ["hI", "Hi"]
            # char_count(lst1) = 2 + 5 = 7
            # char_count(lst2) = 2 + 2 = 4
            # 7 > 4, so lst2 should be returned
            expected_output = ["hI", "Hi"]
            self.assertEqual(mod.total_match(lst1, lst2), expected_output)

    def test_normal_case_2_lst1_shorter(self):
            lst1 = ["hi", "admin"]
            lst2 = ["hi", "hi", "admin", "project"]
            # char_count(lst1) = 2 + 5 = 7
            # char_count(lst2) = 2 + 2 + 5 + 7 = 16
            # 7 < 16, so lst1 should be returned
            expected_output = ["hi", "admin"]
            self.assertEqual(mod.total_match(lst1, lst2), expected_output)

    def test_normal_case_3_lst2_shorter_again(self):
            lst1 = ["hi", "admin"]
            lst2 = ["hI", "hi", "hi"]
            # char_count(lst1) = 2 + 5 = 7
            # char_count(lst2) = 2 + 2 + 2 = 6
            # 7 > 6, so lst2 should be returned
            expected_output = ["hI", "hi", "hi"]
            self.assertEqual(mod.total_match(lst1, lst2), expected_output)

    def test_normal_case_4_single_element_lst1_shorter(self):
            lst1 = ["4"]
            lst2 = ["1", "2", "3", "4", "5"]
            # char_count(lst1) = 1
            # char_count(lst2) = 1 + 1 + 1 + 1 + 1 = 5
            # 1 < 5, so lst1 should be returned
            expected_output = ["4"]
            self.assertEqual(mod.total_match(lst1, lst2), expected_output)

    def test_edge_case_empty_lists(self):
            lst1 = []
            lst2 = []
            # char_count(lst1) = 0
            # char_count(lst2) = 0
            # 0 == 0, so lst1 should be returned
            expected_output = []
            self.assertEqual(mod.total_match(lst1, lst2), expected_output)

    def test_edge_case_equal_length_single_char(self):
            lst1 = ["a"]
            lst2 = ["b"]
            # char_count(lst1) = 1
            # char_count(lst2) = 1
            # 1 == 1, so lst1 should be returned
            expected_output = ["a"]
            self.assertEqual(mod.total_match(lst1, lst2), expected_output)

    def test_edge_case_long_vs_short_strings(self):
            lst1 = ["longstring"]
            lst2 = ["short"]
            # char_count(lst1) = 10
            # char_count(lst2) = 5
            # 10 > 5, so lst2 should be returned
            expected_output = ["short"]
            self.assertEqual(mod.total_match(lst1, lst2), expected_output)

    def test_error_lst1_not_list(self):
            lst1 = None
            lst2 = ["a"]
            with self.assertRaises(TypeError):
                mod.total_match(lst1, lst2)

    def test_error_lst2_not_list(self):
            lst1 = ["a"]
            lst2 = 123
            with self.assertRaises(TypeError):
                mod.total_match(lst1, lst2)

    def test_error_lst1_contains_non_string(self):
            lst1 = ["a", 1, "b"]
            lst2 = ["c"]
            with self.assertRaises(TypeError):
                mod.total_match(lst1, lst2)

    def test_error_lst2_contains_non_string(self):
            lst1 = ["a"]
            lst2 = ["b", None]
            with self.assertRaises(TypeError):
                mod.total_match(lst1, lst2)

