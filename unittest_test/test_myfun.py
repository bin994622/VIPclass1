"""
unittest.main （） 方法

设计TestCase测试用例

@classmethod 方法

"""
# 导入unittest包
import unittest
from unittest_test.myfun import *

# 固定写法--测试用例类要继承unittest.TestCase类
class TestMyFun(unittest.TestCase):
    # 初始化方法 setUp方法     结束工作方法 tearDown
    @classmethod # classmethod 方法
    def setUpClass(cls) -> None:
        print('setUpClass整个测试用例执行前执行一次')

    def setUp(self):
        print('setUp每条测试用例执行前执行一次')

    # 结束工作方法 tearDown
    @classmethod  # 类方法
    def tearDownClass(cls) -> None:
        print('tearDownClass整个测试用例执行后执行一次')

    def tearDown(self) ->None:
        print('tearDown每条测试用例执行后执行一次')


    # 测试用例  方法以test开头
    # 加法
    def test_add(self):
        print('执行测试add方法')
        # 使用断言
        self.assertEqual(add(1, 2), 3)   # add(1,2)为预期结果，3为实际结果，预期结果和实际结果的顺序可以相互变化（实际结果，预期结果）
    # 减法
    def test_minus(self):
        print('执行测试minus方法')
        # 使用断言
        self.assertEqual(2, minus(5, 3))
    # 乘法
    def test_multi(self):
        print('执行测试multi方法')
        # 使用断言
        self.assertEqual(multi(2, 3), 6)
    # 除法
    def test_divide(self):
        print('执行测试divide方法')
        # 使用断言
        self.assertEqual(2, divide(4, 2))
# main方法
if  __name__ == 'main':
    unittest.main()