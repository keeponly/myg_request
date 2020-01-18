# _*_coding: utf-8 _*_
# @Time     :2019/5/17  10:02
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :ddt_suite.py    
import unittest
import HTMLTestRunnerNew
from learn_python.learn_unittest.uitest.l_ddt import TestMsg

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestMsg))
with open('ddt.html', 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                              title='自动化测试报告',
                                              description='ddt使用',
                                              tester='王凯')
    runner.run(suite)
