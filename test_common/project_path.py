# -*-coding:utf-8-*-
# @time     :2019/5/3 16:27
# Author    :lemon_youran
# @Email    :1063699580@qq.com
# @File     :project_path.PY
# @Software :PyCharm
# 文件的路径
import os
# 文件的路径
project_path =os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 测试用例的路径
case_path = os.path.join(project_path, 'test_case', 'test_api.xlsx')
# 测试报告的路径
report_path = os.path.join(project_path, 'test_result', 'test_report', 'test_report.html')
# 测试日志的路径
log_path = os.path.join(project_path, 'test_result', 'test_log', 'mylog.log')
# 配置文件的路径
conf_path = os.path.join(project_path, 'test_conf', 'case.conf')
conf_path_apiurl=os.path.join(project_path,'test_conf','api.conf')
conf_path_username=os.path.join(project_path,'test_conf','envo.conf')