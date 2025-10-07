import unittest
from sut_llm.problem_HumanEval_21 import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):

    def assertListAlmostEqual(self, list1, list2, places=7, msg=None):
        """Helper to compare lists of floats with a tolerance."""
        self.assertEqual(len(list1), len(list2), msg="Lists have different lengths")
        for i, (a, b) in enumerate(zip(list1, list2)):
            self.assertAlmostEqual(a, b, places=places, msg=f"Elements at index {i} differ: {a} != {b}")

    def test_1_basic_increasing_sequence(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected = [0.0, 0.25, 0.5, 0.75, 1.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)

    def test_2_basic_decreasing_sequence(self):
        numbers = [5.0, 4.0, 3.0, 2.0, 1.0]
        expected = [1.0, 0.75, 0.5, 0.25, 0.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)

    def test_3_mixed_order_sequence(self):
        numbers = [3.0, 1.0, 5.0, 2.0, 4.0]
        expected = [0.5, 0.0, 1.0, 0.25, 0.75]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)

    def test_4_sequence_with_negative_numbers(self):
        numbers = [-5.0, -3.0, -1.0, 1.0, 3.0]
        expected = [0.0, 0.25, 0.5, 0.75, 1.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)

    def test_5_all_same_numbers_zero_range(self):
        # Assuming if min_val == max_val, all elements become 0.0
        numbers = [7.0, 7.0, 7.0]
        expected = [0.0, 0.0, 0.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)

    def test_6_only_two_elements(self):
        numbers = [10.0, 20.0]
        expected = [0.0, 1.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)

    def test_7_floats_with_decimals_and_small_range(self):
        numbers = [0.1, 0.2, 0.3, 0.4]
        expected = [0.0, 1/3, 2/3, 1.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)

    def test_8_large_numbers_large_range(self):
        numbers = [1000.0, 1500.0, 2000.0]
        expected = [0.0, 0.5, 1.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)

    def test_9_numbers_including_zero_mixed_signs(self):
        numbers = [-2.0, 0.0, 2.0]
        expected = [0.0, 0.5, 1.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)

    def test_10_complex_sequence_non_uniform_steps(self):
        numbers = [10.0, 12.0, 15.0, 20.0]
        expected = [0.0, 0.2, 0.5, 1.0]
        result = rescale_to_unit(numbers)
        self.assertListAlmostEqual(result, expected)

    def test_rescale_all_numbers_are_same(self):
        # Covers the case where min_val == max_val, leading to range_val == 0
        numbers = [5.0, 5.0, 5.0, 5.0]
        expected = [0.0, 0.0, 0.0, 0.0]
        result = rescale_to_unit(numbers)
        self.assertEqual(result, expected)

    def test_rescale_single_element_list(self):
        # Covers the case of a single element list, which also results in range_val == 0
        numbers = [10.0]
        expected = [0.0]
        result = rescale_to_unit(numbers)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()