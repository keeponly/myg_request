import requests
from ruamel import yaml
import unittest

from test_common.get_data import GetData


class test_q6_secondlogin(unittest.TestCase):
    def test_q6_secondlogin(self):
        """报告审核复审人登录"""

        #url = "https://pg-bate.cailian.net/api/loginNew"
        url = "https://test2-pg.cailian.net/api/loginNew"
        headers = {"Content-Type": "application/json"}
        headers=None
        param ={'loginName':'18600678453','password':'e3ceb5881a0a1fdaad01296d7554868d','kaptchaCode':'1111'}
     # 发送请求
        response = requests.post(url=url, data=param, headers=headers,verify=False)
        print(response.text)
    def test_q6_testingedu_auth(self):
        """报告审核复审人登录"""
        #url = "https://pg-bate.cailian.net/api/loginHandle"
        url = "https://test2-pg.cailian.net/api/loginHandle"
        headers = {"Content-Type": "application/json"}
        param={'companyId':'189','userId':'379'}

        # 发送请求
        response = requests.post(url=url, data=param,verify=False)

        print(response.json()['data']['token'])
        token_fushen=response.json()['data']['token']
        setattr(GetData, "token_fushen", token_fushen)
        print('报告复审人的token的值是>>>>>>>>>>' + token_fushen)



