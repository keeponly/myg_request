import requests
from ruamel import yaml
import unittest

from test_common.get_data import GetData


class test_r4_athirdlogin(unittest.TestCase):
    def test_r4_athirdlogin(self):
        """报告审核签发人登录"""

        #url = "https://pg-bate.cailian.net/api/loginNew"
        url = "https://test2-pg.cailian.net/api/loginNew"
        headers = {"Content-Type": "application/json"}
        headers=None
        param ={'loginName':'13911419652','password':'e3ceb5881a0a1fdaad01296d7554868d','kaptchaCode':'1111'}
     # 发送请求
        response = requests.post(url=url, data=param, headers=headers,verify=False)
        print(response.text)
    def test_r4_athirdlogin(self):
        """报告审核签发人登录"""
        #url = "https://pg-bate.cailian.net/api/loginHandle"
        url = "https://test2-pg.cailian.net/api/loginHandle"
        headers = {"Content-Type": "application/json"}
        param={'companyId':'189','userId':'211'}

        # 发送请求
        response = requests.post(url=url, data=param,verify=False)

        print(response.json()['data']['token'])
        token_qianfa=response.json()['data']['token']
        setattr(GetData, "token_qianfa", token_qianfa)
        print('报告签发人的token的值是>>>>>>>>>>' + token_qianfa)



