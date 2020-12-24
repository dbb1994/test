from common.run_main import handle_request
from utils.handle_response import get_response_content
import json

def getCookie():
    token = input("请输入今天的token：")
    url = 'http://test.mv3.tv.mitvos.com/api/a3/login'
    params = {
        'token': token,
        'uid' : 'basemi_MjE4NTI1NDUzOQ=='
    }
    headers = {
            'Connection': 'close'
        }
    res = handle_request.run_main('GET',url=url,headers=headers,params=params)
    res = get_response_content(res)
    app_token = res['data']['app_token']

    return app_token
