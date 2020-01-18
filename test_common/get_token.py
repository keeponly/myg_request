import yaml
import os
# cur = os.path.dirname(os.path.realpath(__file__))

def get_token(yamlName="Token.yaml"):
    # 从配置文件中读取token值，并返回
    p = os.path.join(r'D:\test\pg_api_master\test_common\Token.yaml')
    f = open(p)
    a = f.read()
    t = yaml.load(a)
    f.close()
    return t["token"]


if __name__ == "__main__":
    get_token()
