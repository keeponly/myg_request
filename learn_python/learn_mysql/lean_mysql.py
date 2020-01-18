# _*_coding: utf-8 _*_
# @Time     :2019/5/24  11:06
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :lean_mysql.py    
# 操作mysql
# pip install mysql-connector-python
# pip install pymysql
# mysql
import pymysql
# 第一步，连接数据库
# 提供数据库的连接信息
db_config = {'host': 'test.lemonban.com',
             'user': 'test',
             'password': 'test',
             'port': 3306,
             'database': 'future',
             'charset': 'utf8'
        }
cnn = pymysql.connect(**db_config)  # 建立连接  ** 传字典   * 传元组
# 第二步获取操作数据库权限
cursor = cnn.cursor()
# 操作数据表
query = 'select * from member where Id  <=100'
# 执行操作
cursor.execute(query)
# 打印数据库查询结果
res = cursor.execute(query)
res2= cursor.fetchone()  # 只获取一条查询结果
res1 = cursor.fetchall()   # 返回元组
print('数据库2查询结果.{}'.format(res2))
print('数据库1查询结果.{}'.format(res1))
print('数据库查询条数.{}'.format(res))
# 增改查 cursor.execute('commit') 提交