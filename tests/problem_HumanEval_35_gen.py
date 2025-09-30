import unittest
from sut.problem_HumanEval_35 import max_element

class TestMaxElement(unittest.TestCase):

    def test_basic_positive_integers(self):
        self.assertEqual(max_element([1, 2, 3]), 3)

    def test_mixed_positive_negative_zero(self):
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

    def test_single_element_list(self):
        self.assertEqual(max_element([7]), 7)

    def test_all_negative_numbers(self):
        self.assertEqual(max_element([-1, -5, -2, -10]), -1)

    def test_duplicate_maximums(self):
        self.assertEqual(max_element([10, 2, 10, 5]), 10)

    def test_zero_as_maximum(self):
        self.assertEqual(max_element([-5, -2, 0, -1]), 0)

    def test_floating_point_numbers(self):
        self.assertEqual(max_element([1.1, 2.2, 0.5, 1.9]), 2.2)

    def test_mixed_integers_and_floats(self):
        self.assertEqual(max_element([1, 2.5, 0, 2, -3.1]), 2.5)

    def test_maximum_at_beginning(self):
        self.assertEqual(max_element([100, 1, 2, 3, 50]), 100)

    def test_maximum_at_end(self):
        self.assertEqual(max_element([1, 2, 3, 50, 100]), 100)

if __name__ == '__main__':
    unittest.main()