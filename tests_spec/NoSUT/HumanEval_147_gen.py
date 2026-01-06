import unittest
from sut.problem_HumanEval_147 import get_max_triples

class Test_get_max_triples(unittest.TestCase):
    def test_normal_case_n5(self):
        # n = 5, expected output = 1
        # Indices x where x % 3 == 2: {2, 5} (count = 2)
        # Indices x where x % 3 != 2: {1, 3, 4} (count = 3)
        # Triples from x % 3 == 2: C(2, 3) = 0
        # Triples from x % 3 != 2: C(3, 3) = 1
        # Total = 0 + 1 = 1
        self.assertEqual(get_max_triples(5), 1)

    def test_normal_case_n8(self):
        # n = 8, expected output = 11
        # Indices x where x % 3 == 2: {2, 5, 8} (count = 3)
        # Indices x where x % 3 != 2: {1, 3, 4, 6, 7} (count = 5)
        # Triples from x % 3 == 2: C(3, 3) = 1
        # Triples from x % 3 != 2: C(5, 3) = 10
        # Total = 1 + 10 = 11
        self.assertEqual(get_max_triples(8), 11)

    def test_edge_case_n1(self):
        # n = 1, too small for any triple
        self.assertEqual(get_max_triples(1), 0)

    def test_edge_case_n2(self):
        # n = 2, too small for any triple
        self.assertEqual(get_max_triples(2), 0)

    def test_edge_case_n3(self):
        # n = 3, a_mod_3 = [1, 0, 1]. No three indices satisfy the condition.
        # Indices x where x % 3 == 2: {2} (count = 1)
        # Indices x where x % 3 != 2: {1, 3} (count = 2)
        # Triples from x % 3 == 2: C(1, 3) = 0
        # Triples from x % 3 != 2: C(2, 3) = 0
        # Total = 0 + 0 = 0
        self.assertEqual(get_max_triples(3), 0)

    def test_edge_case_n4(self):
        # n = 4, a_mod_3 = [1, 0, 1, 1]. One triple (1,3,4) where all a[x]%3==1.
        # Indices x where x % 3 == 2: {2} (count = 1)
        # Indices x where x % 3 != 2: {1, 3, 4} (count = 3)
        # Triples from x % 3 == 2: C(1, 3) = 0
        # Triples from x % 3 != 2: C(3, 3) = 1
        # Total = 0 + 1 = 1
        self.assertEqual(get_max_triples(4), 1)

    def test_error_case_n_zero(self):
        # n must be positive (n >= 1)
        with self.assertRaises(ValueError):
            get_max_triples(0)

    def test_error_case_n_negative(self):
        # n must be positive (n >= 1)
        with self.assertRaises(ValueError):
            get_max_triples(-1)

    def test_error_case_n_float(self):
        # n must be an integer
        with self.assertRaises(TypeError):
            get_max_triples(5.5)

    def test_error_case_n_string(self):
        # n must be an integer
        with self.assertRaises(TypeError):
            get_max_triples("abc")

    def test_large_n(self):
        # n = 100
        # Indices x where x % 3 == 2: {2, 5, ..., 98} (count = 33)
        # Indices x where x % 3 != 2: {1, 3, 4, ..., 100} (count = 67)
        # Triples from x % 3 == 2: C(33, 3) = (33 * 32 * 31) / (3 * 2 * 1) = 11 * 16 * 31 = 5456
        # Triples from x % 3 != 2: C(67, 3) = (67 * 66 * 65) / (3 * 2 * 1) = 67 * 11 * 65 = 47915
        # Total = 5456 + 47915 = 53371
        self.assertEqual(get_max_triples(100), 53371)

    def test_another_normal_case_n7(self):
        # n = 7
        # Indices x where x % 3 == 2: {2, 5} (count = 2)
        # Indices x where x % 3 != 2: {1, 3, 4, 6, 7} (count = 5)
        # Triples from x % 3 == 2: C(2, 3) = 0
        # Triples from x % 3 != 2: C(5, 3) = 10
        # Total = 0 + 10 = 10
        self.assertEqual(get_max_triples(7), 10)