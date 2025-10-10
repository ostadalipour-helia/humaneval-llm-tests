import unittest
from sut.problem_HumanEval_116 import sort_array

class TestSortArray(unittest.TestCase):

    def test_basic_non_negative_mixed_ones(self):
        # Test case from docstring, corrected based on rule: [1, 2, 4, 3, 5]
        # 1 (0b1): 1 one
        # 2 (0b10): 1 one
        # 4 (0b100): 1 one
        # 3 (0b11): 2 ones
        # 5 (0b101): 2 ones
        # Sorted by (ones_count, decimal_value): (1,1), (1,2), (1,4), (2,3), (2,5)
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 4, 3, 5])

    def test_with_zero(self):
        # Test case from docstring, corrected based on rule: [0, 1, 2, 4, 3]
        # 0 (0b0): 0 ones
        # 1 (0b1): 1 one
        # 2 (0b10): 1 one
        # 4 (0b100): 1 one
        # 3 (0b11): 2 ones
        # Sorted by (ones_count, decimal_value): (0,0), (1,1), (1,2), (1,4), (2,3)
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 4, 3])

    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])

    def test_single_element(self):
        self.assertEqual(sort_array([7]), [7])

    def test_all_same_ones_count(self):
        # All numbers have 2 ones: 3 (0b11), 5 (0b101), 6 (0b110)
        # Should sort by decimal value
        self.assertEqual(sort_array([3, 5, 6]), [3, 5, 6])

    def test_all_different_ones_count(self):
        # 1 (1 one), 2 (1 one), 4 (1 one), 3 (2 ones), 7 (3 ones)
        # Should sort primarily by ones count, then decimal
        self.assertEqual(sort_array([1, 2, 3, 4, 7]), [1, 2, 4, 3, 7])

    def test_powers_of_two(self):
        # All numbers are powers of two, thus have 1 one in binary
        # Should sort by decimal value
        self.assertEqual(sort_array([8, 1, 4, 2]), [1, 2, 4, 8])

    def test_large_numbers_mixed(self):
        # 16 (0b10000): 1 one
        # 17 (0b10001): 2 ones
        # 15 (0b1111): 4 ones
        # 31 (0b11111): 5 ones
        # Sorted: (1,16), (2,17), (4,15), (5,31)
        self.assertEqual(sort_array([15, 16, 17, 31]), [16, 17, 15, 31])

    def test_duplicates(self):
        # 1 (1 one), 2 (1 one), 3 (2 ones)
        # Duplicates should maintain their relative order if ones count and value are same (stable sort)
        # or simply be grouped by value if not stable. The problem implies a stable sort for equal keys.
        # (1,1), (1,1), (1,2), (1,2), (2,3)
        self.assertEqual(sort_array([1, 2, 1, 3, 2]), [1, 1, 2, 2, 3])

    def test_all_zeros(self):
        # All zeros, 0 ones each. Should remain sorted by decimal (which they already are)
        self.assertEqual(sort_array([0, 0, 0]), [0, 0, 0])

if __name__ == '__main__':
    unittest.main()