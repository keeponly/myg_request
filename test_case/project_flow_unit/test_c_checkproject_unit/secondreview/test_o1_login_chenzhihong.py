import requests
from ruamel import yaml
import unittest

from test_common.get_data import GetData


class test_o1_login(unittest.TestCase):
    def test_o1_login(self):
        """陈志红登录"""
        #url = "https://pg-bate.cailian.net/api/loginNew"
        url = "https://test2-pg.cailian.net/api/loginNew"
        headers = {"Content-Type": "application/json"}
        headers=None
        param ={'loginName':'13511066395','password':'e3ceb5881a0a1fdaad01296d7554868d','kaptchaCode':'1111'}
     # 发送请求
        response = requests.post(url=url, data=param, headers=headers,verify=False)
        print(response.text)
    def test_o2_testingedu_auth(self):
        """"陈志红登录"""
        #url = "https://pg-bate.cailian.net/api/loginHandle"
        url = "https://test2-pg.cailian.net/api/loginHandle"
        headers = {"Content-Type": "application/json"}
        param={'companyId':'189','userId':'212'}

        # 发送请求
        response = requests.post(url=url, data=param,verify=False)
        token_chenzhihong=response.json()['data']['token']
        print(response.json()['data']['token'])
        setattr(GetData, "token_chenzhihong", token_chenzhihong)
        print('立项复审人token的值是>>>>>>>>>>' + token_chenzhihong)
        print(token_chenzhihong)



