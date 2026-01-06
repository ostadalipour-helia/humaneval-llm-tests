import unittest
from sut.problem_HumanEval_72 import will_it_fly

class Test_will_it_fly(unittest.TestCase):

    def test_normal_palindromic_sum_ok(self):
        q = [3, 2, 3]
        w = 9
        original_q = list(q) # For invariant check
        result = will_it_fly(q, w)
        self.assertEqual(result, True)
        self.assertEqual(q, original_q) # Invariant check

    def test_normal_not_palindromic(self):
        q = [1, 2]
        w = 5
        original_q = list(q) # For invariant check
        result = will_it_fly(q, w)
        self.assertEqual(result, False)
        self.assertEqual(q, original_q) # Invariant check

    def test_normal_palindromic_sum_too_high(self):
        q = [3, 2, 3]
        w = 1
        original_q = list(q) # For invariant check
        result = will_it_fly(q, w)
        self.assertEqual(result, False)
        self.assertEqual(q, original_q) # Invariant check

    def test_edge_empty_list(self):
        q = []
        w = 5
        original_q = list(q) # For invariant check
        result = will_it_fly(q, w)
        self.assertEqual(result, True)
        self.assertEqual(q, original_q) # Invariant check

    def test_edge_single_element_list(self):
        q = [3]
        w = 5
        original_q = list(q) # For invariant check
        result = will_it_fly(q, w)
        self.assertEqual(result, True)
        self.assertEqual(q, original_q) # Invariant check

    def test_edge_sum_exactly_w(self):
        q = [1, 2, 1]
        w = 4
        original_q = list(q) # For invariant check
        result = will_it_fly(q, w)
        self.assertEqual(result, True)
        self.assertEqual(q, original_q) # Invariant check

    def test_edge_negative_numbers(self):
        q = [-1, 0, -1]
        w = -2
        original_q = list(q) # For invariant check
        result = will_it_fly(q, w)
        self.assertEqual(result, True)
        self.assertEqual(q, original_q) # Invariant check

    def test_error_q_not_list(self):
        q = "not a list"
        w = 5
        with self.assertRaises(TypeError):
            will_it_fly(q, w)

    def test_error_w_not_int(self):
        q = [1, 2, 3]
        w = "not an int"
        original_q = list(q) # For invariant check, though error should prevent modification
        with self.assertRaises(TypeError):
            will_it_fly(q, w)
        self.assertEqual(q, original_q) # Invariant check

    def test_error_q_elements_not_int(self):
        q = [1, "a", 3]
        w = 5
        original_q = list(q) # For invariant check, though error should prevent modification
        with self.assertRaises(TypeError):
            will_it_fly(q, w)
        self.assertEqual(q, original_q) # Invariant check