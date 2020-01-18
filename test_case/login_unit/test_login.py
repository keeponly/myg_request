
import unittest
from test_common.http_request import HttpRequests
from test_common.do_excel import DoExcel
from test_common import project_path
from ddt import ddt, data, unpack
from test_common.my_log import Mylog
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 测试登录 ，只有登录才有token
test_data = DoExcel(project_path.case_path, 'login').read_excel('LoginCASE')
My_log = Mylog()
token = None
@ddt
class Login(unittest.TestCase):
    def setUp(self):
        self.T = DoExcel(project_path.case_path, 'login')

    def tearDown(self):
        pass

    @data(*test_data)
    def test_login(self, case):
        """登陆"""
        global TestResult  # 全局变量
        global token
        # 执行测试
        method = case['Method']
        url = case['Url']
        param = eval(case['Params'])
    # 发起测试
        My_log.info('------正在测试{}模块里的第{}条测试用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
        My_log.info('测试数据是{}'.format(case))
        resp = HttpRequests().http_request(method, url, param,verify=False)
        data=resp.json()
        print(data)
        print(data.get('code'))
        if data.get('code')==1:
            return
        data = resp.json()['data']
        print(data)
        if token is None:  # 判断token是否为空
            token = data.get("token")
        print(token)
        #return token
        message= resp.json()["code"]
        print(message)
        #print(type(message))
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
            self.T.write_back(case['CaseId'] + 1, 9, message)
            self.T.write_back(case['CaseId'] + 1, 10, TestResult)
        My_log.info('测试结果是：{}'.format(TestResult))  # http发送请求拿回的实际结果

