import requests
from ruamel import yaml
def login():
    #url = "https://pg-bate.cailian.net/api/loginNew"
    url = "https://test2-pg.cailian.net/api/loginNew"
    headers = {"Content-Type": "application/json"}
    headers=None
    param ={'loginName':'18610933265','password':'e3ceb5881a0a1fdaad01296d7554868d','kaptchaCode':'1111'}
    # 发送请求
    response = requests.post(url=url, data=param, headers=headers,verify=False)
    print(response.text)
def test_testingedu_auth():
    #url = "https://pg-bate.cailian.net/api/loginHandle"
    url = "https://test2-pg.cailian.net/api/loginHandle"
    headers = {"Content-Type": "application/json"}
    param={'companyId':'189','userId':'1187'}

    # 发送请求
    response = requests.post(url=url, data=param,verify=False)

    print(response.text)
    print(response.status_code)
    print(response.json()['data']['token'])

    # 把token值写入配置文件中
    yamlpath = r'D:\test\pg_api_master\test_common\Token.yaml'
    tokenValue = {
        'token':response.json()['data']['token'],
    }
    with open(yamlpath, "w", encoding="utf-8") as f:
        yaml.dump(tokenValue, f, Dumper=yaml.RoundTripDumper)
if __name__ == "__main__":
    login()
    test_testingedu_auth()