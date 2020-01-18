# _*_coding: utf-8 _*_
# @Time     :2019/5/15  17:10
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_ddt.py
# ddt 数据驱动测试 pip install ddt
import unittest
from ddt import ddt, data, unpack
test_data = [[1, 2, 3], [4, 5, 8], [7, 8, 15]]
@ddt
class TestMsg(unittest.TestCase):
    def setUp(self):
        print('----------开始执行测试用例-------------')

    def tearDown(self):
        print('-----------测试用例执行结束------------')

    @data(*test_data)  # ([1, 2, 3], [4, 5, 8], [7, 8, 15])
    @unpack  #下面接收数据的函数，里面的参数个数必须等于里边里的每个元素的子元素个数
    def test_001(self, a, b, expected):
        c = a + b
        try:
            self.assertEqual(c, expected)
        except AssertionError as e:
            print('测试用例执行的错误是{}'.format(e))
            raise e
        print('测试用例的结果是{}'.format(c))


