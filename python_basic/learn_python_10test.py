import unittest
from python_basic import learn_python_10

# from learn_python_10 import get_formatted_name

class NamesTestClass(unittest.TestCase):
    """测试用例"""

    def setUp(self):
        """创建调查对象,供测试方法使用"""
        self.test_first_name = 'brooks'
        self.test_middle_name = "haha"
        self.test_last_name = "lee"

    def test_first_last_name(self):
        """测试是否能够正确处理 Brooks Lee这样的名字"""
        test_formatted_name = learn_python_10.get_formatted_name(self.test_first_name, self.test_last_name)
        #断言
        self.assertEqual(test_formatted_name, "Brooks Lee")

    def test_first_middle_last_name(self):
        """测试是否能够正确处理 Brooks Lee这样的名字"""
        test_formatted_name = learn_python_10.get_formatted_name(self.test_first_name, self.test_last_name, self.test_middle_name)
        #断言
        self.assertEqual(test_formatted_name, "Brookshahalee")

unittest.main