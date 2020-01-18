# _*_coding: utf-8 _*_
# @Time     :2019/6/10  10:10
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :learn_re.py  
# @Software :PyCharm  
from test_common.get_data import GetData
import re
target = "{'mobilephone':'#user_phone#','pwd':'#user_pwd#'}"
p = '#(.*?)#'
while re.search(p , target):
    m = re.search(p, target)
    key = m.group(1)
    value = getattr(GetData, key)
    target = re.sub(p, value, target ,count=1)
print(target)