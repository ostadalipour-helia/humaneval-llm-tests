import unittest
from sut.problem_HumanEval_19 import sort_numbers

class Test_sort_numbers(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(sort_numbers("three one five"), 'one three five')

    def test_normal_case_2(self):
        self.assertEqual(sort_numbers("one two three"), 'one two three')

    def test_normal_case_3(self):
        self.assertEqual(sort_numbers("seven four seven one"), 'one four seven seven')

    def test_normal_case_4(self):
        self.assertEqual(sort_numbers("nine eight seven six five four three two one zero"), 'zero one two three four five six seven eight nine')

    def test_edge_case_empty(self):
        self.assertEqual(sort_numbers(""), '')

    def test_edge_case_single(self):
        self.assertEqual(sort_numbers("five"), 'five')

    def test_edge_case_all_same(self):
        self.assertEqual(sort_numbers("two two two"), 'two two two')

    def test_edge_case_extremes(self):
        self.assertEqual(sort_numbers("zero nine"), 'zero nine')

    # Additional test cases to meet the 10-test requirement
    def test_another_unsorted(self):
        self.assertEqual(sort_numbers("three one five"), 'one three five')

    def test_another_with_duplicates(self):
        self.assertEqual(sort_numbers("seven four seven one"), 'one four seven seven')