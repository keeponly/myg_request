# -*-coding:utf-8-*-
# @time     :2019/4/30 14:43
# Author    :lemon_youran
# @Email    :1063699580@qq.com
# @File     :http_requests.PY
# @Software :PyCharm
import requests
import json
class HttpRequests:
    """该类完成http的post,get请求，并返回结果"""
    def http_request(self, method, url, param,headers=None,verify=False):
        """根据请求方式来确定发起get请求，还是post请求
        url 发送请求的接口地址
        method 请求方式
        param请求参数"""
        if method.upper() == 'GET':
            try:
                resp = requests.get(url, params=param,headers=headers,verify=verify)
            except Exception as e:
                print("get请求时出错了：{}".format(e))
        elif method.upper() == 'POST':
            print(param)
            try:
                resp = requests.post(url,data=param,headers=headers,verify=verify)

            except Exception as e:
                print("post请求时出错了：{}".format(e))
        else:
            print("不支持该种方式")
            resp = None
        return resp
if __name__ == '__main__':
     str1="projectId=7788"
    # str2="projectId=9179254&mainProjectId=9178924&test=1234"
    # import re
    # pattern1=re.compile(".*mainProjectId=\\d+.*")
    # print(pattern1.match(str2))
    # newstr=re.sub("mainProjectId=\\d+","mainProjectId="+str1.split("=")[1],str2)
    # print(newstr)

    # method = 'post'
    # headers={'token':'923FC0CFF48A067CCC2C034714D8D321'}
    # #token='FE722A89B70529468B9AF1388DA681C6'
    # url = 'https://pg-bate.cailian.net/api/sysfunction/functionChildList'
    # param = {'id': '1121594'}
    # #res = requests.post(url,param,headers=headers,verify=False)
    # res = HttpRequests().http_request(method,url,param,headers,verify=False)
    # print(res.json())

     # pattern1 = re.compile(".*mainProjectId=\\d+.*")
     # if (pattern1.match(param1)):
     #     # print(">>>>>>>>>>>>>>>>>>>>>>>")
     #     param1 = re.sub("mainProjectId=\\d+", "mainProjectId=" + projectId.split("=")[1], param1)
     # param = param1.encode("utf-8")
     str2="i am age %(name)s,high%(name)s"%({"name":4})
     print(str2)
     # projectId = getattr(GetData, "projectId")
     # # 占位符，给用例里面的百分号赋值projectID
     # param1 = param1 % projectId
     #
     # print('param1>>>>>>>>>>' + param1 + " projectId:>>>>>>>>>>>>>>>" + projectId)
     # pattern1 = re.compile(".*mainProjectId=\\d+.*")
     # if(pattern1.match(param1)):
     #     #print(">>>>>>>>>>>>>>>>>>>>>>>")
     #     param1 = re.sub("mainProjectId=\\d+","mainProjectId="+projectId.split("=")[1],param1)



