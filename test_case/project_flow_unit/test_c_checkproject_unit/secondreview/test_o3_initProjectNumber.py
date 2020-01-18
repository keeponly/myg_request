# _*_coding: utf-8 _*_
# @Time     :2019/5/24  10:32
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :test_add_loan.py
# 引入单元测试
import unittest
from test_common.get_token import get_token
from test_common.http_request import HttpRequests
from test_common.do_excel import DoExcel
from test_common import project_path
from ddt import ddt, data
from test_common.my_log import Mylog
from test_common.get_data import GetData
# 测试创建项目
from test_common.read_config import ReadConfig
test_data = DoExcel(project_path.case_path, 'initProjectNumber').read_excel('initProjectNumberCASE')
My_log = Mylog()

@ddt
class test_o3_intprojectnumber(unittest.TestCase):
    def setUp(self):
        self.T = DoExcel(project_path.case_path, 'initProjectNumber')

    def tearDown(self):
        pass

    @data(*test_data)
    def test_o3_intprojectnumber(self, case):
        """获取立项号"""
        # 执行测试
        method = case['Method']

        env = ReadConfig(project_path.conf_path_username).get_data('runenv', 'env')
        url1 = ReadConfig(project_path.conf_path_username).get_data('environment', env)
        url = url1 + case['Url']
        print("url的值>>>>>>>>>>>>>>>"+url)

        param1 = (case['Params'])
        print("param1>>>>>>>>>>>>>>>>>"+param1)
        headers = dict(token=getattr(GetData, "token_chenzhihong"))
        headers['Content-type'] = "application/x-www-form-urlencoded"
        print(headers)
    # 发起测试
        if "%" in param1:
            # 使用占位符的方法，没法匹配多个%s
            projectId = getattr(GetData, "projectId")
            print("projectId>>>>>>>>>>>>" + str(projectId))
            param1 = param1 % ({"projectId": projectId})
            param = param1.encode("utf-8")
        else:
            param2 = (case['Params'])
            param = param2.encode("utf-8")

        My_log.info('------正在测试{}模块里的第{}条测试用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
        My_log.info('测试数据是{}'.format(case))
        resp = HttpRequests().http_request(method, url, param, headers, verify=False)
        print("respone>>>>>>>>>>>>>>"+str(resp.json()))

        message = resp.json()["code"]
        # 把项目id放到datatree接口的参数里面

        if case['CaseId']==1:
            projectNumbervalue = resp.json()["data"]["projectNumber"]

            setattr(GetData, "projectNumber", projectNumbervalue)
            print('projectNumber的值是>>>>>>>>>>' + projectNumbervalue)

            originalInvestorId = resp.json()["data"]["companyList"][0]["originalInvestorId"]
            setattr(GetData, "originalInvestorId", originalInvestorId)
            print('originalInvestorId的值>>>>>>>>>>' + str(originalInvestorId))


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

