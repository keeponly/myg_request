
# 反射，可以动态的查看，增加，删除，更改类里面的属性
from test_common import project_path
from test_common.read_config import ReadConfig


class GetData:
    token_chennijia=None#项目负责人的token
    token_chenzhihong=None#立项复审人的token
    token_chushen=None#报告审核初审人的token
    token_fushen=None#报告审核复审人的token
    token_qianfa=None#报告审核签发人的token
    projectId = None
    taskId=None# 立项复审
    projectNumber=None
    originalInvestorId=None
    investorId=None
    id=None
    taskId1=None #附件模式-资产基础法-初审
    taskId2=None#附件模式-拒绝
    taskId3=None#附件模式-审核拒绝之后-添加意见
    taskId4=None#附件模式-审核通过之后-添加意见
    taskId5=None#附件模式-审核通过
    taskId6=None#附件审核-签发通过
    procInstId=None#附件模式-审核拒绝之后-添加意见
    procInstId1=None#附件模式-审核通过之后-添加意见

    user_phone = ReadConfig(project_path.conf_path).get_str('data', 'user_phone')
    user_pwd = ReadConfig(project_path.conf_path).get_str('data', 'user_pwd')
    user_id = ReadConfig(project_path.conf_path).get_str('data', 'user_id')
# 类属性


#print(GetData.user_id)
#print(getattr(GetData, 'token'))
setattr(GetData,'value_id','1234')
#print(getattr(GetData, 'value_id'))
# print(getattr(GetData, 'value_id'))
# print(hasattr(GetData, 'COOKIE'))  # 返回布尔值
# print(setattr(GetData, 'COOKIE', '4567'))  # 修改新的数值，没有返回值
# print(getattr(GetData, 'COOKIE'))
# print(delattr(GetData, 'COOKIE'))  # 删除类的属性
# print(getattr(GetData, 'COOKIE'))

