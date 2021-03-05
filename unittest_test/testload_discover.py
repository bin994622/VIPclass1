"""


testload_discover 方法
"""
import unittest, os
class RunAllCase:
    def run_test(self):

        # 调用defaultTestLoader类中的discover方法,寻找测试集合
        # 路径用'\\',liunx用的是反'/'   三种写法都是可以的
        # 获取路径   当前文件：__file__
        # test_dir = os.path.dirname(__file__)
        suite = unittest.defaultTestLoader.discover("D:\\apitest\VIPclass1\\unittest_test",pattern='test*.py')
        # suite = unittest.defaultTestLoader.discover("D:/apitest/VIPclass1/unittest_test", pattern='test*.py')
        # suite = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
        # 构建测试用例执行机器
        runner = unittest.TextTestRunner()
        # 运行测试用例集合---runner.run()方法
        runner.run(suite)  # 执行的是集合
if __name__ == '__main__':
    # 调用类实例化run_test方法
    RunAllCase().run_test()