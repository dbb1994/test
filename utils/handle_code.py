import yaml
"""
查询常见错误码:输入类型为 int 
"""
code_file = '/Users/wangjin/PycharmProjects/apiauto/config/responce_code.yml'

def search_code(code):
    if code:
        with open(code_file) as c:
           data = yaml.safe_load(c)
           cause = data.get("code").get(code)
        return cause
