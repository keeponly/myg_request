# # _*_coding: utf-8 _*_
#
#
# # 引入单元测试
# import unittest
# import pymysql
# from test_common.http_request import HttpRequests
# from test_common.do_excel import DoExcel
# from test_common import project_path
# from ddt import ddt, data
# from test_common.my_log import Mylog
# from test_common.get_data import GetData
# from test_common.do_mysql import DoMysql
# from test_case.login_unit.test_login import token
#
# from test_common.get_token import   get_token
# from test_common.read_config import ReadConfig
#
# test_data = DoExcel(project_path.case_path, 'selectAllAssessmentObject').read_excel('selectAllAssessmentObjectCASE')
# My_log = Mylog()
#
# @ddt
# class SelectAllAssessmentObject(unittest.TestCase):
#     def setUp(self):
#         self.T = DoExcel(project_path.case_path, 'selectAllAssessmentObject')
#
#     def tearDown(self):
#         pass
#
#     @data(*test_data)
#
#     def test_selectAllAssessmentObject(self, case):
#         """获取项目类型"""
#         global TestResult  # 全局变量
#
#         # 执行测试
#         method = case['Method']
#         env = ReadConfig(project_path.conf_path_username).get_data('runenv', 'env')
#         url1 = ReadConfig(project_path.conf_path_username).get_data('environment', env)
#         url = url1 + case['Url']
#
#         param = eval(case['Params'])
#         print(type(param))
#         print(param)
#         headers= dict(token=get_token())
#         print(headers)
#     # 发起测试
#
#         My_log.info('------正在测试{}模块里的第{}条测试用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
#         My_log.info('测试数据是{}'.format(case))
#         resp = HttpRequests().http_request(method, url, param,headers,verify=False)
#
#         message = resp.json()["code"]
#
#         try:
#             print(type(case['ExpectedResult']))
#             self.assertEqual(str(case['ExpectedResult']), str(message))
#             TestResult = 'pass'
#         except AssertionError as e:
#             TestResult = 'failed'
#             My_log.error('测试执行过程中出错，错误是:{}'.format(e))
#             raise e
#         finally:
#             # 写回结果
#             self.T.write_back(case['CaseId'] + 1, 9, resp.text)
#             self.T.write_back(case['CaseId'] + 1, 10, TestResult)
#         My_log.info('测试结果是：{}'.format(TestResult))  # http发送请求拿回的实际结果
