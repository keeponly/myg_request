import os
import re
'''
Get All Classes' Path
'''


def root_path():
    file_address = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
    root_path = re.search(r'(.*)test_common', file_address)
    return root_path.group(1)


def yaml_path():
    yaml_path = os.path.join(root_path(), 'data/yaml_data/url.yaml')
    if not os.path.exists(yaml_path):
        os.mkdir(yaml_path)
    return yaml_path


def case_path():
    case_path = os.path.join(root_path(), 'test_case/')
    if not os.path.exists(case_path):
        os.mkdir(case_path)
    return case_path


# report's position
def report_path():
    report_path = os.path.join(root_path(), 'test_result')
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    return report_path


def exception_path():
    exception_path = os.path.join(root_path(), 'exception/custom_exception.py')
    if not os.path.exists(exception_path):
        os.mkdir(exception_path)
    return exception_path


def xlsx_path():
    xlsx_path = os.path.join(root_path(), 'data/xlsx_data/data.xlsx')
    if not os.path.exists(xlsx_path):
        os.mkdir(xlsx_path)
    return xlsx_path


def config_path():
    config_path = os.path.join(root_path(), 'public_method/configparse_util.py')
    if not os.path.exists(config_path):
        os.mkdir(config_path)
    return config_path


def filter_path():
    filter_path = os.path.join(root_path(), 'public_method/filter_parse.py')
    if not os.path.exists(filter_path):
        os.mkdir(filter_path)
    return filter_path

def crg_path():
    crg_path = os.path.join(root_path(), 'config_data/config.ini')
    if not os.path.exists(crg_path):
        os.mkdir(crg_path)
    return crg_path

if __name__ == '__main__':
    root_path()
    yaml_path()