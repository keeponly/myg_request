# _*_coding: utf-8 _*_

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

test_data = DoExcel(project_path.case_path, 'create_project').read_excel('CREATECASE')
My_log = Mylog()
token = None
value=""
@ddt
class CreateProject(unittest.TestCase):
    def setUp(self):
        self.T = DoExcel(project_path.case_path, 'create_project')

    def tearDown(self):
        pass

    @data(*test_data)
    def test_create_project(self, case):
        '''创建项目的所有的接口'''
        global TestResult  # 全局变量
        # 执行测试
        method = case['Method']
        env = ReadConfig(project_path.conf_path_username).get_data('runenv', 'env')
        url1 = ReadConfig(project_path.conf_path_username).get_data('environment', env)
        url = url1 + case['Url']
        param = (case['Params'])
        headers = dict(token=get_token())
        headers['Content-type'] = "application/x-www-form-urlencoded"
    # 发起测试

        My_log.info('------正在测试{}模块里的第{}条测试用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
        My_log.info('测试数据是{}'.format(case))
        resp = HttpRequests().http_request(method, url, param, headers, verify=False)
        print(resp.json())
        message = resp.json()["code"]
        print(message)
        # 把项目id放到datatree接口的参数里面
        if case['CaseId']==4:
            #把projectID的值存起来
            projectIdvalue = resp.json()["data"]["projectId"]
            setattr(GetData, "projectId", projectIdvalue)
            print('projectID的值是>>>>>>>>>>' + str(projectIdvalue))
            #把investorId的值存起来
            investorIdvalue=resp.json()["data"]["investorId"]
            setattr(GetData, "investorId", investorIdvalue)
            print('investorId的值是>>>>>>>>>>' + str(investorIdvalue))

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

