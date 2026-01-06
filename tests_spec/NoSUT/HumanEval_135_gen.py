import unittest
from sut.problem_HumanEval_135 import can_arrange

class Test_can_arrange(unittest.TestCase):
    def test_normal_single_disorder(self):
        # A typical case with a single 'disorder' at index 3 (4 > 3).
        arr = [1, 2, 4, 3, 5]
        self.assertEqual(can_arrange(arr), 3)

    def test_normal_multiple_disorders(self):
        # Multiple 'disorders', returning the largest index (6 > 3 at index 4).
        arr = [1, 5, 2, 6, 3]
        self.assertEqual(can_arrange(arr), 4)

    def test_normal_reverse_sorted(self):
        # A fully reverse-sorted array, returning the last possible index.
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(can_arrange(arr), 4)

    def test_edge_already_sorted(self):
        # An already sorted array, no disorder.
        arr = [1, 2, 3]
        self.assertEqual(can_arrange(arr), -1)

    def test_edge_empty_array(self):
        # An empty array, no elements to compare.
        arr = []
        self.assertEqual(can_arrange(arr), -1)

    def test_edge_single_element_array(self):
        # A single-element array, no preceding element for comparison.
        arr = [5]
        self.assertEqual(can_arrange(arr), -1)

    def test_edge_smallest_disorder(self):
        # The smallest possible array with a disorder.
        arr = [3, 2]
        self.assertEqual(can_arrange(arr), 1)

    def test_edge_disorder_then_sorted(self):
        # Disorder at index 1, then sorted again.
        arr = [2, 1, 3]
        self.assertEqual(can_arrange(arr), 1)

    def test_error_non_list_input_none(self):
        # Input 'arr' is not a list (None).
        with self.assertRaises(TypeError):
            can_arrange(None)

    def test_error_non_list_input_string(self):
        # Input 'arr' is not a list (string).
        with self.assertRaises(TypeError):
            can_arrange("hello")

    def test_error_non_comparable_elements(self):
        # Elements of 'arr' are not comparable (mixed types).
        arr = [1, 'a', 3]
        with self.assertRaises(TypeError):
            can_arrange(arr)

    def test_error_non_comparable_elements_objects(self):
        # Elements of 'arr' are not comparable (objects without comparison ops).
        class MyObject:
            def __init__(self, val):
                self.val = val
        arr = [MyObject(1), MyObject(2)]
        with self.assertRaises(TypeError):
            can_arrange(arr)