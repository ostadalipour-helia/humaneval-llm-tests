import unittest
from sut.problem_HumanEval_100 import make_a_pile

class Test_make_a_pile(unittest.TestCase):

    def test_normal_odd_sequence(self):
        n = 3
        expected_output = [3, 5, 7]
        result = make_a_pile(n)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0], n)
        self.assertEqual(result, expected_output)
        for i in range(1, len(result)):
            self.assertEqual(result[i], result[i-1] + 2)
            self.assertEqual(result[i] % 2, n % 2) # Check parity

    def test_normal_even_sequence(self):
        n = 4
        expected_output = [4, 6, 8, 10]
        result = make_a_pile(n)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0], n)
        self.assertEqual(result, expected_output)
        for i in range(1, len(result)):
            self.assertEqual(result[i], result[i-1] + 2)
            self.assertEqual(result[i] % 2, n % 2) # Check parity

    def test_normal_another_odd_sequence(self):
        n = 5
        expected_output = [5, 7, 9, 11, 13]
        result = make_a_pile(n)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0], n)
        self.assertEqual(result, expected_output)
        for i in range(1, len(result)):
            self.assertEqual(result[i], result[i-1] + 2)
            self.assertEqual(result[i] % 2, n % 2) # Check parity

    def test_edge_smallest_positive_n(self):
        n = 1
        expected_output = [1]
        result = make_a_pile(n)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0], n)
        self.assertEqual(result, expected_output)
        # No subsequent elements to check difference for n=1
        self.assertEqual(result[0] % 2, n % 2) # Check parity

    def test_edge_smallest_even_n(self):
        n = 2
        expected_output = [2, 4]
        result = make_a_pile(n)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), n)
        self.assertEqual(result[0], n)
        self.assertEqual(result, expected_output)
        for i in range(1, len(result)):
            self.assertEqual(result[i], result[i-1] + 2)
            self.assertEqual(result[i] % 2, n % 2) # Check parity

    def test_error_n_is_zero(self):
        with self.assertRaises((ValueError, AssertionError)):
            make_a_pile(0)

    def test_error_n_is_negative(self):
        with self.assertRaises((ValueError, AssertionError)):
            make_a_pile(-5)

    def test_error_n_is_float(self):
        with self.assertRaises((TypeError, AssertionError)):
            make_a_pile(3.5)

    def test_error_n_is_string(self):
        with self.assertRaises((TypeError, AssertionError)):
            make_a_pile("abc")