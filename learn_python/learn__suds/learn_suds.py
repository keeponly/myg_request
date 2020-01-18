# -*-coding:utf-8-*-
# @time     :2019/4/30 14:43
# Author    :lemon_youran
# @Email    :1063699580@qq.com
# @File     :http_requests.PY
# @Software :PyCharm
from suds.client import Client
url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
client = Client(url)
print(client)
t = {'client_ip':'1', 'tmpl_id':'0', 'mobile':'15313929271'}
result = client.service.sendMCode(t)
print(result)
