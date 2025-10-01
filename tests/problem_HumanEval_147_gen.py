import unittest
from sut.problem_HumanEval_147 import get_max_triples

class TestGetMaxTriples(unittest.TestCase):

    def test_n_equals_1_no_triples(self):
        # n=1, a=[1]. No triples possible.
        self.assertEqual(get_max_triples(1), 0)

    def test_n_equals_2_no_triples(self):
        # n=2, a=[1, 3]. No triples possible.
        self.assertEqual(get_max_triples(2), 0)

    def test_n_equals_3_no_triples(self):
        # n=3, a=[1, 3, 7]. No triples sum to multiple of 3.
        # a_mod_3 = [1, 0, 1]. C(1,3) + C(2,3) = 0 + 0 = 0.
        self.assertEqual(get_max_triples(3), 0)

    def test_n_equals_4_one_triple(self):
        # n=4, a=[1, 3, 7, 13].
        # a_mod_3 = [1, 0, 1, 1]. (1,7,13) sums to 21 (multiple of 3).
        # count0=1 (for a[2]=3), count1=3 (for a[1]=1, a[3]=7, a[4]=13).
        # C(1,3) + C(3,3) = 0 + 1 = 1.
        self.assertEqual(get_max_triples(4), 1)

    def test_n_equals_5_example_case(self):
        # n=5, a=[1, 3, 7, 13, 21].
        # a_mod_3 = [1, 0, 1, 1, 0]. (1,7,13) sums to 21.
        # count0=2 (for a[2]=3, a[5]=21), count1=3 (for a[1]=1, a[3]=7, a[4]=13).
        # C(2,3) + C(3,3) = 0 + 1 = 1.
        self.assertEqual(get_max_triples(5), 1)

    def test_n_equals_6_four_triples(self):
        # n=6, a=[1, 3, 7, 13, 21, 31].
        # a_mod_3 = [1, 0, 1, 1, 0, 1].
        # count0=2 (a[2]=3, a[5]=21), count1=4 (a[1]=1, a[3]=7, a[4]=13, a[6]=31).
        # C(2,3) + C(4,3) = 0 + 4 = 4.
        self.assertEqual(get_max_triples(6), 4)

    def test_n_equals_7_ten_triples(self):
        # n=7, a=[1, 3, 7, 13, 21, 31, 43].
        # a_mod_3 = [1, 0, 1, 1, 0, 1, 1].
        # count0=2 (a[2]=3, a[5]=21), count1=5 (a[1]=1, a[3]=7, a[4]=13, a[6]=31, a[7]=43).
        # C(2,3) + C(5,3) = 0 + 10 = 10.
        self.assertEqual(get_max_triples(7), 10)

    def test_n_equals_8_eleven_triples(self):
        # n=8, a=[1, 3, 7, 13, 21, 31, 43, 57].
        # a_mod_3 = [1, 0, 1, 1, 0, 1, 1, 0].
        # count0=3 (a[2]=3, a[5]=21, a[8]=57), count1=5 (a[1]=1, a[3]=7, a[4]=13, a[6]=31, a[7]=43).
        # C(3,3) + C(5,3) = 1 + 10 = 11.
        self.assertEqual(get_max_triples(8), 11)

    def test_n_equals_9_twenty_one_triples(self):
        # n=9, a=[1, 3, 7, 13, 21, 31, 43, 57, 73].
        # a_mod_3 = [1, 0, 1, 1, 0, 1, 1, 0, 1].
        # count0=3 (a[2]=3, a[5]=21, a[8]=57), count1=6 (a[1]=1, a[3]=7, a[4]=13, a[6]=31, a[7]=43, a[9]=73).
        # C(3,3) + C(6,3) = 1 + 20 = 21.
        self.assertEqual(get_max_triples(9), 21)

    def test_n_equals_10_thirty_six_triples(self):
        # n=10, a=[1, 3, 7, 13, 21, 31, 43, 57, 73, 91].
        # a_mod_3 = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1].
        # count0=3 (a[2]=3, a[5]=21, a[8]=57), count1=7 (a[1]=1, a[3]=7, a[4]=13, a[6]=31, a[7]=43, a[9]=73, a[10]=91).
        # C(3,3) + C(7,3) = 1 + 35 = 36.
        self.assertEqual(get_max_triples(10), 36)

if __name__ == '__main__':
    unittest.main()