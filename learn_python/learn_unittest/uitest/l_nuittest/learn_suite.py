# -*-coding:utf-8-*-
# @time     :2019/5/5 14:19
# Author    :lemon_youran
# @Email    :1063699580@qq.com
# @File     :learn_suite.PY
# @Software :PyCharm

import HTMLTestRunnerNew
from learn_python.learn_unittest.uitest.l_nuittest import learn_unittest

suite = unittest.TestSuite()  # 创建实例
# suite.addTest(TestAdd('test_001'))  # 第一种方式添加用例
# suite.addTest(TestAdd('test_002'))
# suite.addTest(TestSub('test_003'))

loader = unittest.TestLoader()
# 第二种方式添加用例
# suite.addTest(loader.loadTestsFromTestCase(TestAdd))
# suite.addTest(loader.loadTestsFromTestCase(TestSub))
# 第三种方式添加用例
suite.addTest(loader.loadTestsFromModule(learn_unittest))
# with open('test.txt', 'w', encoding='utf-8') as file:
#     runner = unittest.TextTestRunner(stream=file, verbosity=2)  # 执行用例
#     runner.run(suite)
# runner = unittest.TextTestRunner()  # 执行用例
# runner.run(suite)

# file = open('testlog.txt', 'w')
# try:
#     print(a)
# except Exception as e:
#     file.write(str(e))
#     raise e
with open('test_0304.html','wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                              title='2019自动化测试报告',
                                              description='2019第一次自动化测试',
                                              tester='王凯')
    runner.run(suite)