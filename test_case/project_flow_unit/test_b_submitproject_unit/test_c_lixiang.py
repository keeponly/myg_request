# _*_coding: utf-8 _*_
# @Time     :2019/5/24  10:32
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :test_add_loan.py
# 引入单元测试
import unittest
import pymysql
import re
from test_case.project_flow_unit.test_a_createproject_unit.test_a_create_project import value
from test_common.http_request import HttpRequests
from test_common.do_excel import DoExcel
from test_common import project_path
from ddt import ddt, data
from test_common.my_log import Mylog
from test_common.get_data import GetData
from test_common.do_mysql import DoMysql

from test_common.read_config import ReadConfig

from test_common.get_token import   get_token

test_data = DoExcel(project_path.case_path, 'lixiang').read_excel('lixiangCASE')
My_log = Mylog()

@ddt
class LiXiang(unittest.TestCase):
    def setUp(self):
        self.T = DoExcel(project_path.case_path, 'lixiang')

    def tearDown(self):
        pass

    @data(*test_data)

    def test_lixiang(self, case):
        """"立项提交的所有接口"""
        global TestResult  # 全局变量
        #global token
        # 执行测试
        getattr(GetData, 'value_id')
        method = case['Method']
        env = ReadConfig(project_path.conf_path_username).get_data('runenv', 'env')
        url1 = ReadConfig(project_path.conf_path_username).get_data('environment', env)
        url = url1 + case['Url']

        param1 = (case['Params'])
        print(type(param1))
        if "%" in param1:

            projectId = getattr(GetData, "projectId")
            print("projectId>>>>>>>>>>>>" + str(projectId))
            param1 = param1 % ({"projectId": projectId})
            param = param1.encode("utf-8")
        else:

            param2 = (case['Params'])
            param = param2.encode("utf-8")

        headers= dict(token=get_token())
        headers['Content-type'] = "application/x-www-form-urlencoded"

    # 发起测试

        My_log.info('------正在测试{}模块里的第{}条测试用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
        My_log.info('测试数据是{}'.format(case))
        resp = HttpRequests().http_request(method, url, param,headers,verify=False)
        message = resp.json()["code"]
        try:
            print(type(case['ExpectedResult']))
            self.assertEqual(str(case['ExpectedResult']), str(message))
            TestResult = 'pass'
        except AssertionError as e:
            TestResult = 'failed'
            My_log.error('测试执行过程中出错，错误是:{}'.format(e))
            raise e
        finally:
            # 写回结果
            self.T.write_back(case['CaseId'] + 1, 9, resp.text)
            self.T.write_back(case['CaseId'] + 1, 10, TestResult)
        My_log.info('测试结果是：{}'.format(TestResult))  # http发送请求拿回的实际结果
