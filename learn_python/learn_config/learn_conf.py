# _*_coding: utf-8 _*_
# @Time     :2019/5/20  17:22
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_conf.py
from configparser import ConfigParser


class ReadConfig:
    def read_config(self):
        cf = ConfigParser()
        cf.read('case.conf', encoding='utf-8')
        res = cf.get('CASE', 'button')
        print(res)


if __name__ == '__main__':
    ReadConfig().read_config()
