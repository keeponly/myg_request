import requests
from ruamel import yaml
import unittest

from test_common.get_data import GetData


class test_o7_login(unittest.TestCase):
    def test_o7_login(self):
        """chennijia"""
        #url = "https://pg-bate.cailian.net/api/loginNew"
        url = "https://test2-pg.cailian.net/api/loginNew"
        headers = {"Content-Type": "application/json"}
        headers=None
        param ={'loginName':'18610933265','password':'e3ceb5881a0a1fdaad01296d7554868d','kaptchaCode':'1111'}
     # 发送请求
        response = requests.post(url=url, data=param, headers=headers,verify=False)
        print(response.text)
    def test_o7_testingedu_auth(self):
        """"chennijia"""
        #url = "https://pg-bate.cailian.net/api/loginHandle"
        url = "https://test2-pg.cailian.net/api/loginHandle"
        headers = {"Content-Type": "application/json"}
        param={'companyId':'189','userId':'1187'}

        # 发送请求
        response = requests.post(url=url, data=param,verify=False)
        token_chennijia=response.json()['data']['token']
        setattr(GetData, "token_chennijia", token_chennijia)
        print('项目送审人token的值是>>>>>>>>>>' + token_chennijia)
        print(token_chennijia)


