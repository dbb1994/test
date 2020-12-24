import json
from common.run_main import HandleRequest


"""通用的断言"""
def assert_common(res,exp_code = 200):
    code = res.status_code
    result = json.loads(res.text)
    assert exp_code == res.status_code ,"状态码不是200"
    assert result.get("msg") == 'success' or 'ok',"msg信息不是success或ok"
    assert result.get("result") == 1 , "result不等于0 "

def assert_uncomon(res):
    code = res.status_code
    assert code != 200

headers = {
    'Connection': 'close'
}
api = '/api/a3/home'
base_url = 'http://test.mv3.tv.mitvos.com' + api
data = {
    'base_url':base_url,
    'headers':headers
}
res = HandleRequest().run_main('GET',url = base_url,headers = headers)

a = assert_common(res)