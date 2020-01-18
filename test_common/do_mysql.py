# _*_coding: utf-8 _*_
# @Time     :2019/5/27  10:35
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :do_mysql.py    
import pymysql
from test_common.read_config import ReadConfig
from test_common import project_path


class DoMysql:
    """操作数据库的类，专门进行数据库读取"""
    def do_mysql(self, query, flag=1):
        """query aql查询语句
        flag 标志1 获取一条数据，2获取多条数据"""
        db_config = ReadConfig(project_path.conf_path).get_data('DB', 'db_config')
        cnn = pymysql.connect(**db_config)
        cursor = cnn.cursor()
        cursor.execute(query)

        if flag == 1:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()
        return res


if __name__ == '__main__':
    query = 'select MAX(Id) from loan where MemberID =3041'
    res = DoMysql().do_mysql(query, 1)
    print('数据库查询结果.{}'.format(res))