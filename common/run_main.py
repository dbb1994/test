import requests

class HandleRequest:
    def __init__(self):
        """保持session"""
        self.session = requests.session()

    def close_session(self):
        self.session.close()

    def post(self,**kwargs):
        params = kwargs.get("params")
        data = kwargs.get("data")
        json = kwargs.get("json")
        headers =  kwargs.get("headers")
        url = kwargs.get("url")
        try:
            result = self.session.post(url,params=params,data=data,json=json,headers=headers)
            return result
        except Exception as e:
            print("post请求错误>>>>",e)

    def get(self,**kwargs):
        params = kwargs.get("params")
        url = kwargs.get("url")
        headers = kwargs.get("headers")
        try:
            result = self.session.get(url=url,params=params,headers=headers)
            return result
        except Exception as e:
            print("get请求错误>>>>",e)

    def run_main(self,method,**kwargs):
        if method == "POST":
            res = self.post(**kwargs)
            return res
        else:
            res = self.get(**kwargs)
            return res

handle_request = HandleRequest()

# headers = {
#     'Connection': 'close'
# }
# api = '/api/a3/home'
# base_url = 'http://test.mv3.tv.mitvos.com' + api
# data = {
#     'base_url':base_url,
#     'headers':headers
# }
# res = HandleRequest().run_main('GET',url = base_url,headers = headers)
#
# print(res)