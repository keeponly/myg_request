from BeautifulReport import BeautifulReport
import unittest
import os
import time

import sys
sys.path.append("../")
from test_common.files_path import case_path, report_path, root_path
#from tomorrow import threads
'''
get numbers from function 'get_count' and add threads()
(Need to fix it)
'''


# 获得所有的单元测试类
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path(), pattern="test*.py", top_level_dir=None)
    return discover


# 获得单元测试类的文件数量
def get_count():
    root = root_path()
    unit_path = root+"test_common/"
    dir_list = os.listdir(unit_path)
    count = len(dir_list)-1
    return count

# 多线程启动单元测试
#@threads(get_count())
def run():
    now_time = time.strftime('%Y_%m_%d %H_%M_%S', time.localtime(time.time()))
    result = BeautifulReport(all_case())
    result.report(filename=now_time, description='pg3.0_TestReport', log_path=report_path())

#写回



if __name__ == '__main__':
    run()

