import json
"""
查询要测试的case是否预设了预期结果
"""
json_file = '/Users/wangjin/PycharmProjects/apiauto/data/expect.json'

def seacrh_tag(tag):
    with open(json_file) as j:
        data = json.loads(j.read())
        tags = list(data.keys())
        if tag in tags:
            result = "EXIST"
        else:
            result = "NOT FOUND"
    return result


