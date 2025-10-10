import unittest
from sut.problem_HumanEval_9 import rolling_max


class TestRollingMax(unittest.TestCase):

    def test_example_from_docstring(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2]), [1, 2, 3, 3, 3, 4, 4])

    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element_list(self