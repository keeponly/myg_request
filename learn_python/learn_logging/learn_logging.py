# _*_coding: utf-8 _*_
# @Time     :2019/5/17  17:26
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_logging.py    
import logging
# root logger日志收集器 默认 root logger
# 日志输出渠道 控制台 ,txt，file, test.log
# 1定义一个日志收集齐并设置级别
my_logger = logging.getLogger('pyhon14')  # 定义一个日志收集器
my_logger.setLevel('INFO')  # 设置日志等级
# 2指定输出渠道 StreamHandler---控制台   FileHandle 指定文件
formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[%(name)s]-[日志信息]:%(message)s')
ch = logging.StreamHandler()
ch.setLevel('INFO')
ch.setFormatter(formatter)
# 3指定文件路径
fh = logging.FileHandler('test.log', encoding='utf-8')
fh.setLevel('INFO')
# 4对接
my_logger.addHandler(ch)  # 将收集到的信息发送到指定的渠道
my_logger.addHandler(fh)
# 日志级别
my_logger.debug('我的错误等级1')
my_logger.info('我的错误等级2')
my_logger.warning('我的错误等级3')
my_logger.error('我的错误等级4')
my_logger.critical('我的错误等级5')
# 5用完了移除日志 A AB ABC 不移除的话下次再写入会将上次的再次一起写入一次，移除的是缓存
my_logger.removeHandler(fh)
my_logger.removeHandler(ch)
