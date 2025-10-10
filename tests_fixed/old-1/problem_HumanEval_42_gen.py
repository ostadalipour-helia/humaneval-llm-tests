import unittest
from sut_llm.problem_HumanEval_42 import incr_list

class TestIncrList(unittest.TestCase):

    def test_example_one(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])

    def test_example_two(self):
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

    def test_empty_list(self):
        self.assertEqual(incr_list([]), [])

    def test_single_element_list(self):
        self.assertEqual(incr_list([0]), [1])

    def test_list_with_negative_numbers(self):
        self.assertEqual(incr_list([-1, -2, -3]), [0, -1, -2])

    def test_list_with_mixed_numbers(self):
        self.assertEqual(incr_list([-5, 0, 5]), [-4, 1, 6])

    def test_list_with_large_numbers(self):
        self.assertEqual(incr_list([999999, 1000000]), [1000000, 1000001])

    def test_list_with_duplicate_numbers(self):
        self.assertEqual(incr_list([7, 7, 7]), [8, 8, 8])

    def test_list_with_zero_only(self):
        self.assertEqual(incr_list([0, 0, 0, 0]), [1, 1, 1, 1])

    def test_list_with_one_element_negative(self):
        self.assertEqual(incr_list([-10]), [-9])

if __name__ == '__main__':
    unittest.main()