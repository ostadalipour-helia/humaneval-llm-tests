import unittest
from sut.problem_HumanEval_19 import sort_numbers


class TestSortNumbers(unittest.TestCase):

    def test_basic_case_from_docstring(self):
        self.assertEqual(sort_numbers('three one five'), 'one three five')

    def test_empty_string(self):
        self.assertEqual(sort_numbers(''), '')

    def test_single_number(self):
        self.assertEqual(sort_numbers('seven'), 'seven')

    def test_multiple_unique_unsorted(self):
        self.assertEqual(sort_numbers('nine two four one eight'), 'one two four eight nine')

    def test_with_duplicates(self):
        self.assertEqual(sort_numbers('two one two three'), 'one two two three')

    def test_already_sorted(self):
        self.assertEqual(sort_numbers('one two three'), 'one two three')

    def test_reverse_order(self):
        self.assertEqual(sort_numbers('nine eight seven'), 'seven eight nine')

    def test_all_same_number(self):
        self.assertEqual(sort_numbers('five five five'), 'five five five')

    def test_includes_zero_mixed_order(self):
        self.assertEqual(sort_numbers('four zero nine one'), 'zero one four nine')

    def test_all_numbers_shuffled(self):
        self.assertEqual(sort_numbers('nine eight seven six five four three two one zero'),
                         'zero one two three four five six seven eight nine')


if __name__ == '__main__':
    unittest.main()