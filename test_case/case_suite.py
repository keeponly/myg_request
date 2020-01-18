# _*_coding: utf-8 _*_
# @Time     :2019/5/17  16:18
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :case_suite.py

import sys

from test_case.case_suite1 import test_dir

sys.path.append('./')
import unittest
import HTMLTestRunnerNew
from test_common import project_path

from test_case.project_flow_unit.createproject_unit import test_addproject
# from test_case.test_recharge import TestCase

suite = unittest.TestSuite()
loader = unittest.TestLoader()
#suite.addTest(loader.loadTestsFromTestCase(TestCase))

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)

"""
1、因为unittest中规定，测试用例必须test开头，所以discover中的pattern格式才是test*.py
2、start_dir是存放测试用例的目录
"""

with open(project_path.report_path, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                              title='蘑菇云自动化测试报告',
                                              description='蘑菇云自动化测试报告',
                                              tester='3333')
    runner.run(suite)
