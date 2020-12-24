import json
from deepdiff import DeepDiff
import requests

json_file = '/Users/wangjin/PycharmProjects/apiauto/data/expect.json'

"""
完全校验：格式必须完全一致，内容可以发生变化
"""
def check_json_com(realres, tag):
    with open(json_file) as j:
        exp_datas = json.loads(j.read())
        expectres = exp_datas[tag]
    diffs = DeepDiff(realres, expectres)
    if diffs.get("values_changed") and len(diffs) == 1:
        """格式一致，仅仅是值的内容改变"""
        result = "SUCCESS"
    elif diffs == {}:
        """数据和格式均一致"""
        result = "SUCCESS"
    else:
        """数据和格式均不一致"""
        result = 'FAIL'

    return result

"""
不完全校验，格式粗略的一致，内容的形式或值可以不一致
"""
def check_json_incom(realres,tag):
    with open(json_file) as j:
        """根据tag去查询相应的返回值，并将返回值的key取成一个列表"""

        exp_datas = json.loads(j.read())
        exp_datas = exp_datas[tag]  #取要比较的预期结果数据
        exp_keys = exp_datas.keys()
        """比较实际返回值的key是否包含在预期返回值的key中"""
        if set(realres).issubset(set(exp_keys)):
            result = "SUCCESS"
        else:
            result = "FAIL"
        return result

# res = requests.get(url='http://test.mv3.tv.mitvos.com/api/a3/feed/op-distribute-recom')
# res = json.loads(res.text)
# keys = list(res.keys())
# print(keys)
# a = check_json_incom(keys,'feed/op-distribute-recom')
# print(a)

# a =check_json_style(res,'feed/op-round-test')
# # print(a)
