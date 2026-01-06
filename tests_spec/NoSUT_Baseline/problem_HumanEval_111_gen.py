import unittest
import sut.problem_HumanEval_111 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            """
            Test case for an empty input string.
            Should return an empty dictionary.
            (Edge Case, Return Value)
            """
            self.assertEqual(mod.histogram(''), {})

    def test_single_letter(self):
            """
            Test case for a string with a single letter.
            Should return a dictionary with that letter and count 1.
            (Edge Case, Off-by-One for count, Return Value)
            """
            self.assertEqual(mod.histogram('a'), {'a': 1})

    def test_all_distinct_letters_count_one(self):
            """
            Test case where all letters are distinct, resulting in a max count of 1.
            All letters should be returned with count 1.
            (Boundary: max count 1, multiple letters; Logic: all conditions true for max=1)
            """
            self.assertEqual(mod.histogram('a b c'), {'a': 1, 'b': 1, 'c': 1})

    def test_two_letters_same_max_count_greater_than_one(self):
            """
            Test case with two letters having the same maximum count, which is greater than 1.
            Both letters should be returned.
            (Boundary: max count > 1, multiple letters; Logic: `==` for adding multiple maxes)
            """
            self.assertEqual(mod.histogram('a b b a'), {'a': 2, 'b': 2})

    def test_one_letter_clear_max_count(self):
            """
            Test case where only one letter has the highest count.
            Only that letter should be returned.
            (Boundary: max count > 1, single letter; Logic: `>` for updating max)
            """
            self.assertEqual(mod.histogram('b b b b a'), {'b': 4})

    def test_multiple_letters_two_have_max_count(self):
            """
            Test case with several letters, where two have the same maximum count.
            Both maximum count letters should be returned.
            (Typical, Logic: `==` for adding multiple maxes, `>` for updating max)
            """
            self.assertEqual(mod.histogram('a b c a b'), {'a': 2, 'b': 2})

    def test_single_distinct_letter_repeated_many_times(self):
            """
            Test case with a single distinct letter repeated many times.
            Verifies correct counting for high frequencies.
            (Extreme, Off-by-One for count, Boundary: high count)
            """
            self.assertEqual(mod.histogram('z z z z z z z z z z'), {'z': 10})

    def test_mixed_counts_multiple_maxes(self):
            """
            Test case with mixed counts, where multiple letters share the highest frequency.
            Ensures all letters with the max count are captured, even if they appear later.
            (Logic: `==` for adding multiple maxes, `>` for updating max)
            """
            self.assertEqual(mod.histogram('x y y z z x'), {'x': 2, 'y': 2, 'z': 2})

    def test_mixed_counts_single_max(self):
            """
            Test case with various counts, ensuring only the absolute maximum is returned.
            Catches off-by-one errors in count comparison logic.
            (Logic: `>` for updating max; Off-by-one for counts)
            """
            self.assertEqual(mod.histogram('a b b c c c d d d d e'), {'d': 4})

    def test_long_string_complex_maxes(self):
            """
            Test case with a long string containing many distinct letters, all with the same high max count.
            Verifies correct handling of numerous maximums in a larger input.
            (Extreme, Boundary: many distinct letters, all with same high max count)
            """
            self.assertEqual(mod.histogram('p y t h o n p y t h o n p y t h o n p y t h o n'),
                             {'p': 4, 'y': 4, 't': 4, 'h': 4, 'o': 4, 'n': 4})
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_basic_unique_letters(self):
            # Normal case: multiple unique letters, all with frequency 1
            self.assertEqual(mod.histogram("a b c"), {"a": 1, "b": 1, "c": 1})

    def test_normal_multiple_max_frequency(self):
            # Normal case: two letters with the same maximum frequency
            self.assertEqual(mod.histogram("a b b a"), {"a": 2, "b": 2})

    def test_normal_single_max_frequency(self):
            # Normal case: one letter with the highest frequency
            self.assertEqual(mod.histogram("b b b b a"), {"b": 4})

    def test_normal_complex_multiple_max(self):
            # Normal case: more complex input with multiple letters at max frequency
            self.assertEqual(mod.histogram("m n o p m n o m"), {"m": 3})

    def test_edge_empty_string(self):
            # Edge case: empty input string
            self.assertEqual(mod.histogram(""), {})

    def test_edge_single_letter(self):
            # Edge case: single letter input
            self.assertEqual(mod.histogram("a"), {"a": 1})

    def test_edge_all_same_letter(self):
            # Edge case: all letters are the same
            self.assertEqual(mod.histogram("a a a a a"), {"a": 5})

    def test_edge_alternating_multiple_max(self):
            # Edge case: alternating letters, both at max frequency
            self.assertEqual(mod.histogram("a b a b a b"), {"a": 3, "b": 3})

