import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):

    '跑两个测试用例'
    def test_first_last_name(self):
        formatted_name = get_formatted_name("li","yang")
        self.assertEqual(formatted_name,"Li Yang")


    def test_first_last_name2(self):
        formatted_name = get_formatted_name("shuyuan","he")
        self.assertEqual(formatted_name,"Shuyuan He")

unittest.main()