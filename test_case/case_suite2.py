
# suite = unittest.TestSuite()
# all_cases = unittest.defaultTestLoader.discover(PY_PATH,'Test*.py')
# #discover()方法会自动根据测试目录匹配查找测试用例文件（Test*.py）,并将查找到的测试用例组装到测试套件中
# suite.addTests(case) for case in all_cases
# report_html = BeautifulReport.BeautifulReport(suite)
import unittest

suite = unittest.TestLoader().discover("test_case")

if __name__ == '__main__':
    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
