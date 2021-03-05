"""
单个测试用例执行


unittest.TestSuite()---创建测试用例集合，赋值给suite
suite.addTest(TestMyFun('test_add'))  # 类名(test方法名字)---将测试用例方法加入到测试用例集
runner = unittest.TextTestRunner()-----# 构建测试用例执行机器，赋值给runner
runner.run(suite)   # 执行的是集合----# 运行测试用例集合---runner.run()方法

suite.addTest(TestMyFun('test_add'))  # 类名(test方法名字)---将测试用例方法加入到测试用例集一条

suite.addTest([TestMyFun('test_add'),TestMyFun('test_add'),TestMyFun('test_add')])  # 类名(test方法名字)---将测试用例方法加入到测试用例集多条


"""
# 导入unittest包
import unittest
from unittest_test.myfun import *

# 固定写法--测试用例类要继承unittest.TestCase类
class TestMyFun(unittest.TestCase):
    # # 初始化方法 setUp方法     结束工作方法 tearDown
    # @classmethod # classmethod 方法
    # def setUpClass(cls) -> None:
    #     print('setUpClass整个测试用例执行前执行一次')
    #
    # def setUp(self):
    #     print('setUp每条测试用例执行前执行一次')
    #
    # # 结束工作方法 tearDown
    # @classmethod  # 类方法
    # def tearDownClass(cls) -> None:
    #     print('tearDownClass整个测试用例执行后执行一次')
    #
    # def tearDown(self) ->None:
    #     print('tearDown每条测试用例执行后执行一次')


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
if  __name__ == '__main__':
    # 创建测试用例集合
    suite = unittest.TestSuite()
    # 将测试用例方法加入到测试用例集一条
    suite.addTest(TestMyFun('test_add'))  # 类名(test方法名字)
    # 将测试用例方法加入到测试用例集多条
    # suite.addTest([TestMyFun('test_add'),])  # 类名(test方法名字)
    # 构建测试用例执行机器
    runner = unittest.TextTestRunner()
    # 运行测试用例集合---runner.run()方法
    runner.run(suite)   # 执行的是集合