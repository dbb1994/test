from common.run_main import handle_request
from utils.handle_json import check_json_com,check_json_incom
from utils.handle_tag import seacrh_tag
from utils.handle_code import search_code
import pytest
import allure
import json


@allure.feature("页面数据测试")
class TestHomePage:

    headers = {
        'Connection': 'close',
    }
    api = '/api/a3/home'

    @allure.story("首页底tab - 数据正确性校验")
    @pytest.mark.Home_BottomTab_1
    def test_home_bottom_tab_1(self,getHost):
        base_url = getHost + self.api
        res = handle_request.run_main('GET',url = base_url,headers=self.headers)
        res_code = res.status_code
        if res_code == 200:
            res = json.loads(res.text)
            if res["result"] == 1 and res["msg"] == "OK":
                result = check_json_com(res,tag='home')
                assert result == 'SUCCESS'
                print("接口返回正常，数据正确")
        else:
            cause = search_code(res_code)
            print("接口返回状态码非200：",cause)

    @allure.story("首页底tab - 异常传参测试")
    @pytest.mark.Home_BottomTab_2
    @pytest.mark.parametrize("test_params",['test','009','$^$##^_+_?><','null',''],ids = ['非法传参','非法传参','非法传参','参数传null','参数传空'])
    def test_home_bottom_tab_2(self, getHost,test_params):
        base_url = getHost + self.api
        params = {
            'test': test_params
        }

        res = handle_request.run_main('GET', url=base_url,headers=self.headers,params=params)
        res_code = res.status_code
        if res_code == 200:
            res = json.loads(res.text)
            if res["result"] == 1 and res["msg"] == "OK":
                result = check_json_com(res, tag='home')
                assert result == 'SUCCESS'
                print("接口返回正常，数据正确")
        else:
            cause = search_code(res_code)
            print("接口返回状态码非200：", cause)

class TestFeed:

    headers = {
        'Connection': 'close',
    }
    api = '/api/a3/feed/'

    @allure.story("feed流 - 合法传参")
    @pytest.mark.Feed
    @pytest.mark.parametrize("req_id",['op-distribute-recom','op-recom-ai','op-tv-recom'],ids = ['合法传参：推荐页面','XX页面','XX页面'])
    def test_feed_1(self,getHost,req_id):
        base_url = getHost + self.api + req_id
        tag = 'feed/' + req_id
        if seacrh_tag(tag) == 'EXIST':
            res = handle_request.run_main('GET',url = base_url,headers=self.headers)
            res_code = res.status_code
            if res_code == 200:
                res = json.loads(res.text)
                if res['msg'] == 'OK' and res['result'] == 1:
                    result = check_json_incom(res,tag)
                    assert result == 'SUCCESS'
                    print("接口返回正常，数据正确")
            else:
                cause = search_code(res_code)
                print("接口返回状态码非200：", cause)
                print("失败的req_id", req_id)
        else:
            print("断言失败，未添加预期结果，请重新添加")
            assert 1 == 0

    @allure.story("feed流 - 传入错误的req_id")
    @pytest.mark.Feed
    @pytest.mark.parametrize("req_id",['hdhsdjsjd','null','2931290e2udhwjbdjdbcuwhweowiqowieowhdwdfhdbvshb'],ids=['参数未定义','参数传null','参数超长'])
    def test_feed_2(self,getHost,req_id):
        base_url = getHost + self.api + req_id
        res = handle_request.run_main('GET', url=base_url, headers=self.headers)
        res_code = res.status_code
        if res_code == 200:
            res = json.loads(res.text)
            pytest.assume(res["err_msg"] == 'Find object error: id is not matched')
            pytest.assume(res["result"] == 0)
            print("非法传参校验通过")
        else:
            cause = search_code(res_code)
            print("接口返回状态码非200：", cause)
            print("非法传参校验不通过")

    @allure.story("feed流 - 必填参数req_id未传")
    @pytest.mark.Feed
    @pytest.mark.parametrize("req_id", [''],ids=['未传参数'])
    def test_feed_3(self, getHost, req_id):
        base_url = getHost + self.api + req_id
        res = handle_request.run_main('GET', url=base_url, headers=self.headers)
        res_code = res.status_code
        if res_code:
            assert res_code == 404
            print("必填参数未传校验通过")