import unittest
from sut.problem_HumanEval_23 import strlen

class TestStrlen(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_short_string(self):
        self.assertEqual(strlen('abc'), 3)

    def test_single_character_string(self):
        self.assertEqual(strlen('x'), 1)

    def test_string_with_spaces(self):
        self.assertEqual(strlen('hello world'), 11)

    def test_string_with_leading_trailing_spaces(self):
        self.assertEqual(strlen('  test  '), 8)

    def test_string_with_special_characters(self):
        self.assertEqual(strlen('!@#$%^&*()'), 10)

    def test_string_with_numbers(self):
        self.assertEqual(strlen('1234567890'), 10)

    def test_long_alphanumeric_string(self):
        self.assertEqual(strlen('abcdefghijklmnopqrstuvwxyz0123456789'), 36)

    def test_string_with_unicode_characters(self):
        self.assertEqual(strlen('你好世界'), 4)

    def test_string_with_mixed_case(self):
        self.assertEqual(strlen('PyThOn PrOgRaMmInG'), 18)

if __name__ == '__main__':
    unittest.main()