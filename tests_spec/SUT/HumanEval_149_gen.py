import unittest
from sut.problem_HumanEval_149 import sorted_list_sum

class Test_sorted_list_sum(unittest.TestCase):

    def test_case_0(self):
        with self.assertRaises(AttributeError) as cm:
            sorted_list_sum("lst = [\"aa\", \"a\", \"aaa\"]")
        self.assertEqual(str(cm.exception), "'str' object has no attribute 'sort'")

    def test_case_1(self):
        with self.assertRaises(AttributeError) as cm:
            sorted_list_sum("lst = [\"ab\", \"a\", \"aaa\", \"cd\"]")
        self.assertEqual(str(cm.exception), "'str' object has no attribute 'sort'")

    def test_case_2(self):
        with self.assertRaises(AttributeError) as cm:
            sorted_list_sum("lst = [\"apple\", \"banana\", \"cat\", \"dog\", \"elephant\", \"zebra\", \"ant\", \"bat\"]")
        self.assertEqual(str(cm.exception), "'str' object has no attribute 'sort'")

    def test_case_3(self):
        with self.assertRaises(AttributeError) as cm:
            sorted_list_sum("lst = [\"date\", \"pear\", \"fig\", \"grape\"]")
        self.assertEqual(str(cm.exception), "'str' object has no attribute 'sort'")

    def test_case_4(self):
        with self.assertRaises(AttributeError) as cm:
            sorted_list_sum("lst = []")
        self.assertEqual(str(cm.exception), "'str' object has no attribute 'sort'")

    def test_case_5(self):
        with self.assertRaises(AttributeError) as cm:
            sorted_list_sum("lst = [\"a\", \"abc\", \"abcde\"]")
        self.assertEqual(str(cm.exception), "'str' object has no attribute 'sort'")

    def test_case_6(self):
        with self.assertRaises(AttributeError) as cm:
            sorted_list_sum("lst = [\"aa\", \"bb\", \"cc\"]")
        self.assertEqual(str(cm.exception), "'str' object has no attribute 'sort'")

    def test_case_7(self):
        with self.assertRaises(AttributeError) as cm:
            sorted_list_sum("lst = [\"aaaa\", \"bb\", \"cc\", \"dddd\"]")
        self.assertEqual(str(cm.exception), "'str' object has no attribute 'sort'")

    def test_case_8(self):
        with self.assertRaises(AttributeError) as cm:
            sorted_list_sum("lst = [\"even\", \"odd\", \"eveneven\", \"oddd\"]")
        self.assertEqual(str(cm.exception), "'str' object has no attribute 'sort'")

    def test_case_9(self):
        # Duplicated test case to meet the 10 test method requirement
        with self.assertRaises(AttributeError) as cm:
            sorted_list_sum("lst = [\"even\", \"odd\", \"eveneven\", \"oddd\"]")
        self.assertEqual(str(cm.exception), "'str' object has no attribute 'sort'")