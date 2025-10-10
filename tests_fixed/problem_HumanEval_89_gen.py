import unittest
from sut_llm.problem_HumanEval_89 import encrypt

class TestEncryptFunction(unittest.TestCase):

    def test_example_hi(self):
        # Typical input, given example
        self.assertEqual(encrypt('hi'), 'lm')

    def test_example_asdfghjkl(self):
        # Typical input, given example
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')

    def test_empty_string(self):
        # Edge case: empty string
        self.assertEqual(encrypt(''), '')

    def test_single_char_a_boundary(self):
        # Boundary test: first letter of alphabet
        self.assertEqual(encrypt('a'), 'e')

    def test_single_char_z_wraparound_boundary(self):
        # Boundary test: last letter of alphabet, verifies wrap-around
        self.assertEqual(encrypt('z'), 'd')

    def test_chars_near_wraparound_boundary(self):
        # Boundary test: characters just before and at wrap-around point
        self.assertEqual(encrypt('wxyz'), 'abcd')

    def test_mixed_case_and_non_alpha_logic(self):
        # Logic mutation: ensures only lowercase letters are encrypted, others unchanged
        self.assertEqual(encrypt('Hello World! 123'), 'Hipps Wsvph! 123')

    def test_all_same_char_edge_case(self):
        # Edge case: string with all identical characters
        self.assertEqual(encrypt('aaaaa'), 'eeeee')

    def test_long_string_with_spaces_extreme(self):
        # Extreme input: a longer sentence with spaces
        # The shift amount is 4 (2 * 2).
        # Let's manually verify the expected output:
        # 'the' -> 'xli'
        # 'quick' -> q(16)+4=u(20), u(20)+4=y(24), i(8)+4=m(12), c(2)+4=g(6), k(10)+4=o(14) -> 'uymgo'
        # 'brown' -> b(1)+4=f(5), r(17)+4=v(21), o(14)+4=s(18), w(22)+4=a(0), n(13)+4=r(17) -> 'fvsar'
        # 'fox' -> f(5)+4=j(9), o(14)+4=s(18), x(23)+4=b(1) -> 'jsb'
        # 'jumps' -> j(9)+4=n(13), u(20)+4=y(24), m(12)+4=q(16), p(15)+4=t(19), s(18)+4=w(22) -> 'nyqtw'
        # 'over' -> o(14)+4=s(18), v(21)+4=z(25), e(4)+4=i(8), r(17)+4=v(21) -> 'sziv'
        # 'the' -> 'xli'
        # 'lazy' -> l(11)+4=p(15), a(0)+4=e(4), z(25)+4=d(3), y(24)+4=c(2) -> 'pedc'
        # 'dog' -> d(3)+4=h(7), o(14)+4=s(18), g(6)+4=k(10) -> 'hsk'
        # Combining these, the correct expected string is 'xli uymgo fvsar jsb nyqtw sziv xli pedc hsk'.
        # The original test had incorrect expected values for 'quick', 'over', and 'lazy'.
        self.assertEqual(encrypt('the quick brown fox jumps over the lazy dog'), 'xli uymgo fvsar jsb nyqtw sziv xli pedc hsk')

    def test_only_non_alpha_chars_extreme(self):
        # Extreme input: string with only non-alphabetic characters
        self.assertEqual(encrypt('12345!@#$%^&*()'), '12345!@#$%^&*()')