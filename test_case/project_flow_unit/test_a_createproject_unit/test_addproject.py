# _*_coding: utf-8 _*_
# @Time     :2019/5/24  10:32
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :test_add_loan.py
# 引入单元测试

import unittest
import pymysql
from test_common.http_request import HttpRequests
from test_common.do_excel import DoExcel
from test_common import project_path
from ddt import ddt, data
from test_common.my_log import Mylog
from test_common.get_data import GetData
from test_common.do_mysql import DoMysql
from test_case.login_unit.test_login import token
from test_common.read_config import ReadConfig

from test_common.get_token import get_token

test_data = DoExcel(project_path.case_path, 'create_addproject').read_excel('addproject')
My_log = Mylog()


@ddt
class AddProject(unittest.TestCase):
    def setUp(self):
        self.T = DoExcel(project_path.case_path, 'create_addproject')

    def tearDown(self):
        pass

    @data(*test_data)

    def test_addproject(self, case):
        """创建项目合同价的校验"""
        global TestResult  # 全局变量
        global value  # 全局变量 创建项目后获取的项目ID

        # 执行测试
        method = case['Method']
        env = ReadConfig(project_path.conf_path_username).get_data('runenv', 'env')
        url1 = ReadConfig(project_path.conf_path_username).get_data('environment', env)
        url = url1 + case['Url']

        param = (case['Params'])

        headers= dict(token=get_token())
        headers['Content-type']="application/x-www-form-urlencoded"

    # 发起测试
        My_log.info('------正在测试{}模块里的第{}条测试用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
        My_log.info('测试数据是{}'.format(case))
        resp = HttpRequests().http_request(method, url, param,headers,verify=False)
        print(resp.json())

        message = resp.json()["code"]
        print(message)
        #把项目id放到datatree接口的参数里面
        # projectIdvalue=resp.json()["data"]["projectId"]
        # value="projectId"+"="+str(projectIdvalue)
        # setattr(GetData,"projectId",value)
        # print('vaue的值是>>>>>>>>>>'+value)
        # self.Z=DoExcel(project_path.case_path, 'dataTree')
        # self.Z.write_back(2, 6, str(value))
        # #把项目id放到chaozhao接口中
        # self.Z = DoExcel(project_path.case_path, 'chaozhao')
        # self.Z.write_back(2, 6, str(value))
        # self.Z.write_back(6, 6, str(value))
        # self.Z.write_back(8, 6, str(value))
        # self.Z.write_back(9, 6, str(value))
        # self.Z.write_back(10, 6, str(value))
        # #把项目id放到clickit接口中
        # self.Z = DoExcel(project_path.case_path, 'clickedit')
        # self.Z.write_back(2, 6, str(value))
        # self.Z.write_back(5, 6, str(value))
        # self.Z.write_back(7, 6, str(value))
        # self.Z.write_back(8, 6, str(value))
        # #把项目id放入projectinfo接口中
        # self.Z = DoExcel(project_path.case_path, 'projectinfo')
        # self.Z.write_back(4, 6, str(value))
        # self.Z.write_back(5, 6, str(value))
        # self.Z.write_back(6, 6, str(value))
        # self.Z.write_back(8, 6, str(value))
        # self.Z.write_back(9, 6, str(value))
        # #把项目id放入到lixiang接口中
        # self.Z = DoExcel(project_path.case_path, 'lixiang')
        # self.Z.write_back(2, 6, str(value))
        # self.Z.write_back(3, 6, str(value))
        # self.Z.write_back(5, 6, str(value))
        # self.Z.write_back(6, 6, str(value))
        # self.Z.write_back(8, 6, str(value))
        # self.Z.write_back(9, 6, str(value))
        # #把项目id放入到clickproject接口中
        # self.Z = DoExcel(project_path.case_path, 'clickproject')
        # self.Z.write_back(2, 6, str(value))
        # self.Z.write_back(4, 6, str(value))
        # self.Z.write_back(5, 6, str(value))

        # print(type(message))
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
