# -*-coding:utf-8-*-
# @time     :2019/5/5 13:40
# Author    :lemon_youran
# @Email    :1063699580@qq.com
# @File     :learn_unittest.PY
# @Software :PyCharm

import unittest


class TestAdd(unittest.TestCase):

    def setUp(self):
        print('----开始测试了----')

    def tearDown(self):
        print('----测试结束了----')

    def test_001(self):
        a = 1
        b = 2
        expected = 3
        c = a+b
        try:
            self.assertEqual(expected, c)
        except AssertionError as e:
            print('001用例失败，错误是{}'.format(e))
            raise e
        print('第一条测试结果是{}'.format(c))
#
#     def test_002(self):
#         aa = 22
#         bb = 11
#         expected = 11
#         cc = aa-bb
#         try:
#             self.assertEqual(expected, cc)
#         except AssertionError as e:
#             print('002用例执行失败，错误是{}'.format(e))
#             raise e
#         print('第二条测试结果是{}'.format(cc))
#
#
# class TestSub(unittest.TestCase):
#
#     def test_003(self):
#         aa = 22
#         bb = 1
#         expected = 20
#         cc = aa - bb
#         try:
#             self.assertEqual(expected, cc)
#         except AssertionError as e:
#             print('003测试执行出错，错误是{}'.format(e))
#             raise e  # 将处理结果异常抛出
#         print('第三条测试结果是{}'.format(cc))
