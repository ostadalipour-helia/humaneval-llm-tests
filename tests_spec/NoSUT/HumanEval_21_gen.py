import unittest
from sut.problem_HumanEval_21 import rescale_to_unit

class Test_rescale_to_unit(unittest.TestCase):

    def assertListAlmostEqual(self, list1, list2, places=7, msg=None):
        """Helper to compare two lists of floats with almost equal assertion."""
        self.assertEqual(len(list1), len(list2), msg="Lists have different lengths")
        for i, (a, b) in enumerate(zip(list1, list2)):
            self.assertAlmostEqual(a, b, places=places, msg=f"Elements at index {i} differ: {a} != {b}")

    def test_standard_increasing_positives(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected = [0.0, 0.25, 0.5, 0.75, 1.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)
        self.assertEqual(len(result), len(numbers), "Returned list length mismatch.")

    def test_mixed_signs(self):
        numbers = [-10.0, 0.0, 10.0]
        expected = [0.0, 0.5, 1.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)
        self.assertEqual(len(result), len(numbers), "Returned list length mismatch.")

    def test_decreasing_order(self):
        numbers = [5.0, 4.0, 3.0, 2.0, 1.0]
        expected = [1.0, 0.75, 0.5, 0.25, 0.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)
        self.assertEqual(len(result), len(numbers), "Returned list length mismatch.")

    def test_two_elements(self):
        numbers = [10.0, 20.0]
        expected = [0.0, 1.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)
        self.assertEqual(len(result), len(numbers), "Returned list length mismatch.")

    def test_all_identical_elements(self):
        numbers = [5.0, 5.0, 5.0]
        expected = [0.0, 0.0, 0.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)
        self.assertEqual(len(result), len(numbers), "Returned list length mismatch.")

    def test_already_unit_range(self):
        numbers = [0.0, 0.5, 1.0]
        expected = [0.0, 0.5, 1.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)
        self.assertEqual(len(result), len(numbers), "Returned list length mismatch.")

    def test_all_identical_non_zero_floats(self):
        numbers = [1.234, 1.234, 1.234, 1.234]
        expected = [0.0, 0.0, 0.0, 0.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)
        self.assertEqual(len(result), len(numbers), "Returned list length mismatch.")

    def test_empty_list_error(self):
        numbers = []
        with self.assertRaises((ValueError, IndexError)):
            rescale_to_unit(numbers)

    def test_single_element_list_error(self):
        numbers = [1.0]
        with self.assertRaises((ValueError, IndexError)):
            rescale_to_unit(numbers)

    def test_list_of_integers_error(self):
        numbers = [1, 2, 3]
        with self.assertRaises(TypeError):
            rescale_to_unit(numbers)

    def test_list_of_strings_error(self):
        numbers = ["a", "b", "c"]
        with self.assertRaises(TypeError):
            rescale_to_unit(numbers)