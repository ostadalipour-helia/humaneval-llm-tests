import unittest
from sut_llm.problem_HumanEval_18 import how_many_times

class TestHowManyTimes(unittest.TestCase):

    def test_empty_string_non_empty_substring(self):
        self.assertEqual(how_many_times('', 'a'), 0)

    def test_single_char_substring_multiple_non_overlapping(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)

    def test_multi_char_substring_multiple_overlapping(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

    def test_substring_not_found(self):
        self.assertEqual(how_many_times('hello world', 'xyz'), 0)

    def test_single_occurrence(self):
        self.assertEqual(how_many_times('apple pie', 'app'), 1)

    def test_multiple_overlapping_occurrences_complex(self):
        self.assertEqual(how_many_times('banana banana', 'ana'), 4)

    def test_multiple_non_overlapping_occurrences_distinct_pattern(self):
        self.assertEqual(how_many_times('ababab', 'ab'), 3)

    def test_empty_substring_non_empty_string(self):
        self.assertEqual(how_many_times('python', ''), 0)

    def test_substring_longer_than_string(self):
        self.assertEqual(how_many_times('short', 'longer_substring'), 0)

    def test_string_and_substring_are_identical(self):
        self.assertEqual(how_many_times('exact_match', 'exact_match'), 1)

if __name__ == '__main__':
    unittest.main()