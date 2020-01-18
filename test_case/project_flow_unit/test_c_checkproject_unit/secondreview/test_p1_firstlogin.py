import requests
from ruamel import yaml
import unittest

from test_common.get_data import GetData


class test_p1_login(unittest.TestCase):
    def test_p1_login(self):
        """报告审核初审人登录"""

        #url = "https://pg-bate.cailian.net/api/loginNew"
        url = "https://test2-pg.cailian.net/api/loginNew"
        headers = {"Content-Type": "application/json"}
        headers=None
        param ={'loginName':'13321197081','password':'6846860684f05029abccc09a53cd66f1','kaptchaCode':'1111'}
     # 发送请求
        response = requests.post(url=url, data=param, headers=headers,verify=False)
        print(response.text)
    def test_p1_testingedu_auth(self):
        """报告审核初审人登录"""
        #url = "https://pg-bate.cailian.net/api/loginHandle"
        url = "https://test2-pg.cailian.net/api/loginHandle"
        headers = {"Content-Type": "application/json"}
        param={'companyId':'189','userId':'238'}

        # 发送请求
        response = requests.post(url=url, data=param,verify=False)

        print(response.json()['data']['token'])
        token_chushen=response.json()['data']['token']
        setattr(GetData, "token_chushen", token_chushen)
        print('报告初审人的token的值是>>>>>>>>>>' + token_chushen)



