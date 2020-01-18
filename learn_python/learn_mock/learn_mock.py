# _*_coding: utf-8 _*_
# @Time     :2019/6/11  11:09
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_mock.py  
# @Software :PyCharm  

import unittest
from unittest import mock
from learn_python.learn_mock import payment

class PaymenTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pay_success(self):  # 支付成功
        pay = payment.Payment()
        pay.requestOutofSystem = mock.Mock(return_value = 200)
        resp = pay.doPay(user_id=1, card_num='123456', amount=100)
        self.assertEqual('success', resp)

    def test_pay_fail(self):
        pay = payment.Payment()
        pay.requestOutofSystem = mock.Mock(return_value=500)
        resp = pay.doPay(user_id=1, card_num='123456', amount=200)
        self.assertEqual('fail', resp)
        pay.requestOutofSystem.assert_called()
        pay.requestOutofSystem.assert_called_with('123456', 200)

    def test_pay_retry_success(self):
        pay = payment.Payment()
        pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 200])
        resp = pay.doPay(user_id=1, card_num='123456', amount=100)
        print('调用次数', pay.requestOutofSystem.call_count)
        print('调用参数', pay.requestOutofSystem.call_args)
        self.assertEqual('success', resp)

    def test_pay_retry_fail(self):
        pay = payment.Payment()
        pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError, 500])
        resp = pay.doPay(user_id=1, card_num='123456', amount=100)
        self.assertEqual('fail', resp)
