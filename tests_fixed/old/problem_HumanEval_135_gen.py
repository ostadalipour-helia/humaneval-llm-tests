import unittest
from sut_llm.problem_HumanEval_135 import can_arrange

class TestCanArrange(unittest.TestCase):

    def test_example_one(self):
        self.assertEqual(can_arrange([1,2,4,3,5]), 3)

    def test_example_two_strictly_increasing(self):
        self.assertEqual(can_arrange([1,2,3]), -1)

    def test_decreasing_pair_at_end(self):
        self.assertEqual(can_arrange([1,2,3,5,4]), 4)

    def test_decreasing_pair_at_beginning(self):
        self.assertEqual(can_arrange([2,1,3,4,5]), 1)

    def test_multiple_decreasing_pairs_returns_largest_index(self):
        self.assertEqual(can_arrange([1,5,3,4,2]), 4)

    def test_two_elements_decreasing(self):
        self.assertEqual(can_arrange([2,1]), 1)

    def test_two_elements_increasing(self):
        self.assertEqual(can_arrange([1,2]), -1)

    def test_three_elements_decreasing_in_middle(self):
        self.assertEqual(can_arrange([1,3,2]), 2)

    def test_all_elements_decreasing(self):
        self.assertEqual(can_arrange([5,4,3,2,1]), 4)

    def test_longer_array_with_scattered_decreasing_pairs(self):
        self.assertEqual(can_arrange([1, 8, 3, 9, 5, 10, 7]), 6)