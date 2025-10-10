import unittest
from sut_llm.problem_HumanEval_147 import get_max_triples

class TestGetMaxTriples(unittest.TestCase):

    def test_edge_case_n_equals_1(self):
        # n=1: a = [1]. No triples possible.
        self.assertEqual(get_max_triples(1), 0)

    def test_edge_case_n_equals_2(self):
        # n=2: a = [1, 3]. No triples possible.
        self.assertEqual(get_max_triples(2), 0)

    def test_boundary_case_n_equals_3(self):
        # n=3: a = [1, 3, 7]. Only one combination (1,3,7). Sum = 11, not multiple of 3.
        self.assertEqual(get_max_triples(3), 0)

    def test_boundary_case_n_equals_4(self):
        # n=4: a = [1, 3, 7, 13].
        # (1,7,13) -> 1+7+13 = 21 (multiple of 3). This is the only one.
        self.assertEqual(get_max_triples(4), 1)

    def test_typical_case_n_equals_5_from_docstring(self):
        # n=5: a = [1, 3, 7, 13, 21].
        # Docstring example: (1, 7, 13) is the only valid triple. Sum = 21.
        self.assertEqual(get_max_triples(5), 1)

    def test_typical_case_n_equals_6(self):
        # n=6: a = [1, 3, 7, 13, 21, 31].
        # Values % 3: [1, 0, 1, 1, 0, 1]
        # Triples (a[i]%3, a[j]%3, a[k]%3) must be (0,0,0) or (1,1,1)
        # Indices for 0-remainder: [1, 4] (values 3, 21)
        # Indices for 1-remainder: [0, 2, 3, 5] (values 1, 7, 13, 31)
        # (0,0,0) type: C(2,3) = 0
        # (1,1,1) type: C(4,3) = 4. All sums are multiples of 3.
        # Total: 4
        self.assertEqual(get_max_triples(6), 4)

    def test_extreme_case_n_equals_7_many_triples_of_one_type(self):
        # n=7: a = [1, 3, 7, 13, 21, 31, 43].
        # Values % 3: [1, 0, 1, 1, 0, 1, 1]
        # Indices for 0-remainder: [1, 4] (values 3, 21)
        # Indices for 1-remainder: [0, 2, 3, 5, 6] (values 1, 7, 13, 31, 43)
        # (0,0,0) type: C(2,3) = 0
        # (1,1,1) type: C(5,3) = 10. All sums are multiples of 3.
        # Total: 10
        self.assertEqual(get_max_triples(7), 10)

    def test_extreme_case_n_equals_8_mixed_triple_types(self):
        # n=8: a = [1, 3, 7, 13, 21, 31, 43, 57].
        # Values % 3: [1, 0, 1, 1, 0, 1, 1, 0]
        # Indices for 0-remainder: [1, 4, 7] (values 3, 21, 57)
        # Indices for 1-remainder: [0, 2, 3, 5, 6] (values 1, 7, 13, 31, 43)
        # (0,0,0) type: C(3,3) = 1. (3,21,57) sum=81.
        # (1,1,1) type: C(5,3) = 10.
        # Total: 1 + 10 = 11
        self.assertEqual(get_max_triples(8), 11)

    def test_boundary_case_n_equals_9_increase_in_one_remainder_type(self):
        # n=9: a = [1, 3, 7, 13, 21, 31, 43, 57, 73].
        # Values % 3: [1, 0, 1, 1, 0, 1, 1, 0, 1]
        # Indices for 0-remainder: [1, 4, 7] (values 3, 21, 57)
        # Indices for 1-remainder: [0, 2, 3, 5, 6, 8] (values 1, 7, 13, 31, 43, 73)
        # (0,0,0) type: C(3,3) = 1.
        # (1,1,1) type: C(6,3) = 20.
        # Total: 1 + 20 = 21
        self.assertEqual(get_max_triples(9), 21)

    def test_extreme_case_n_equals_10_larger_input(self):
        # n=10: a = [1, 3, 7, 13, 21, 31, 43, 57, 73, 91].
        # Values % 3: [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
        # Indices for 0-remainder: [1, 4, 7] (values 3, 21, 57)
        # Indices for 1-remainder: [0, 2, 3, 5, 6, 8, 9] (values 1, 7, 13, 31, 43, 73, 91)
        # (0,0,0) type: C(3,3) = 1.
        # (1,1,1) type: C(7,3) = 35.
        # Total: 1 + 35 = 36
        self.assertEqual(get_max_triples(10), 36)