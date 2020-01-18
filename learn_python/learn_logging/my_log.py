# _*_coding: utf-8 _*_
# @Time     :2019/5/20  16:37
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :my_log.py    
import logging


class Mylog:
    def my_log(self,lever, msg):
        my_logger = logging.getLogger('python14')
        my_logger.setLevel('DEBUG')
        formatter = logging.Formatter('[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[%(name)s]-[日志信息]:%(message)s')
        ch = logging.StreamHandler()
        ch.setLevel('INFO')
        ch.setFormatter(formatter)
        fh = logging.FileHandler('mylog.log', encoding='utf-8')
        fh.setLevel('INFO')
        fh.setFormatter(formatter)
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if lever == 'DEBUG':
            my_logger.debug(msg)
        elif lever == 'INFO':
            my_logger.info(msg)
        elif lever == 'WARNING':
            my_logger.warning(msg)
        elif lever == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)
        my_logger.addHandler(fh)
        my_logger.removeHandler(fh)
        my_logger.removeHandler(ch)

    def debug(self, msg):
        self.my_log('DEBUG', msg) # 直接调用my_log函数

    def info(self, msg):
        self.my_log('INFO', msg)


if __name__ == '__main__':
    my_logger = Mylog()
    my_logger.info('日志优化')


