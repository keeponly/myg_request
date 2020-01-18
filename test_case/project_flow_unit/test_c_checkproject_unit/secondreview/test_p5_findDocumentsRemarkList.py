import unittest
from test_common.get_token import get_token
from test_common.http_request import HttpRequests
from test_common.do_excel import DoExcel
from test_common import project_path
from ddt import ddt, data
from test_common.my_log import Mylog
from test_common.get_data import GetData
from test_common.do_mysql import DoMysql
from test_common.read_config import ReadConfig
test_data = DoExcel(project_path.case_path, 'findDocumentsRemarkList').read_excel('findDocumentsRemarkListCASE1')
My_log = Mylog()
token = None
@ddt
class test_p5_findDocumentsRemarkList(unittest.TestCase):
    def setUp(self):
        self.T = DoExcel(project_path.case_path, 'findDocumentsRemarkList')
    def tearDown(self):
        pass
    @data(*test_data)
    def test_p5_findDocumentsRemarkList(self, case):
        '''获取拒绝的taskid'''
        global TestResult  # 全局变量
        # 执行测试
        method = case['Method']
        env = ReadConfig(project_path.conf_path_username).get_data('runenv', 'env')
        url1 = ReadConfig(project_path.conf_path_username).get_data('environment', env)
        url = url1 + case['Url']
        param1 = (case['Params'])

        headers = dict(token=getattr(GetData, "token_chushen"))
        headers['Content-type'] = "application/x-www-form-urlencoded"

        # 发起测试
        if "%" in param1:
            # 使用占位符的方法，没法匹配多个%s
            projectId = getattr(GetData, "projectId")
            investorId = getattr(GetData,"investorId")
            print("projectId:{},investorId:{}".format(projectId,investorId))
            param1 = param1 % ({"projectId": projectId,"investorId":investorId})
            param = param1.encode("utf-8")
        else:
            param2 = (case['Params'])
            param = param2.encode("utf-8")

        My_log.info('------正在测试{}模块里的第{}条测试用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
        My_log.info('测试数据是{}'.format(case))
        resp = HttpRequests().http_request(method, url, param, headers, verify=False)
        print("response>>>>>>>>>>>>>>>>>" + str(resp.json()))
        message = resp.json()["code"]

        if case['CaseId']==2:
            #公司初审的taskid
            taskId2value = resp.json()["data"]["taskId"]
            setattr(GetData, "taskId2", taskId2value)
            print('taskId2的值是>>>>>>>>>>' + taskId2value)

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

