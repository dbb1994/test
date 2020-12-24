from common.run_main import handle_request
from utils.handle_json import check_json_com,check_json_incom
from utils.handle_tag import seacrh_tag
from utils.asserts import assert_common,assert_uncomon
import pytest
import allure
import json
import random
import ast

@allure.feature("播放历史模块测试")
class TestHistory:

    headers = {
        'Connection': 'close'
    }
    api = '/api/a3/play_record/'

    @allure.story("上传播放历史测试 - 合法传参")
    @pytest.mark.Send_Record
    @pytest.mark.run(order=1)
    def test_send_record_1(self,getHost):
        base_url = getHost + self.api + 'send_record'
        params={
            "_session":'KRVCks2TzQz5_IS-u7rRzBAg2kAbg4rdsYVTSwWTJA_v6Jn0Nl_aI1lcOs7KUNEnkS0tKk2EkjCbDTXr7HffqA==',
        }
        body = [{
            "cp": "iqiyi",
            "last_play_time": 1608560826582,
            "play_count": 2,
            "progress": 333,
            "ref": "com.miui.video",
            "video": "nv-00004@NV000000713475",
            "video_id": "NV000000713475"
        }]
        res = handle_request.run_main('POST',url=base_url,params=params,json=body)
        assert_common(res)
        result = json.loads(res.text)
        # print(result)
        assert result.get("data")[0] == body[0].get("video_id")

    @allure.story("上传播放历史测试 - 非法传参")
    @pytest.mark.Send_Record
    # @pytest.mark.parametrize("param",[None,'','disididsidxxxxxx',2323333345344])
    @pytest.mark.flaky(6)
    def test_send_record_2(self, getHost):
        base_url = getHost + self.api + 'send_record'
        params = {
            "_session": 'KRVCks2TzQz5_IS-u7rRzBAg2kAbg4rdsYVTSwWTJA_v6Jn0Nl_aI1lcOs7KUNEnkS0tKk2EkjCbDTXr7HffqA==',
        }
        random_param = [None,'','disididsidxxxxxx',2323333345344]
        body = [{
            "cp": random.choice(random_param),
            "last_play_time": random.choice(random_param),
            "play_count": random.choice(random_param),
            "progress": random.choice(random_param),
            "ref": random.choice(random_param),
            "video": random.choice(random_param),
            "video_id": random.choice(random_param)
        }]
        print("BODY",body)
        res = handle_request.run_main('POST', url=base_url, params=params, json=body)
        assert_uncomon(res)

    # @allure.story("获取播放历史测试 - 数据正确性校验")
    # @pytest.mark.Get_Record
    # @pytest.mark.parametrize("page_no,video_type",[(0,0),(0,1),(0,2)],ids=['全部视频','长视频','短视频'])
    # @pytest.mark.run(order=2)
    # def test_get_record_1(self, getHost,page_no,video_type):
    #     base_url = getHost + self.api + 'get_record'
    #     params = {
    #         'page_no': page_no,
    #         'video_type':video_type,
    #         '_session': 'KRVCks2TzQz5_IS-u7rRzBAg2kAbg4rdsYVTSwWTJA9r5byziNvDPLLnJvNp75boPK5AB1ivRb2pgEV-TbWvzA=='
    #     }
    #     res = handle_request.run_main('GET',url = base_url,params = params,headers = self.headers)
    #     res = json.loads(res.text)
    #     result = check_json_incom(res,'record/get_record')
    #     data = res.get('data')[0]
    #     progress = data.get("progress")
    #     assert result == 'SUCCESS'
    #     pytest.assume(progress == 333)
    #     # print(res.get("data")
    #     # pytest.assume(res["data"][0].get("progress") == 333)
    #
    # @allure.story("获取播放历史测试 - 必传字段不传")
    # @pytest.mark.Get_Record
    # @pytest.mark.parametrize("params",['',None],ids=['参数为空','参数为None'])
    # def test_get_record_2(self, getHost,params):
    #     base_url = getHost + self.api + 'get_record'
    #     res = handle_request.run_main('GET',url = base_url,params=params,headers = self.headers)
    #     pytest.assume(res.status_code == 200)
    #     res = json.loads(res.text)
    #     pytest.assume(res["msg"] == 'Unauthorized')
    #
    # @allure.story("获取播放历史测试 - 必传字段非法")
    # @pytest.mark.Get_Record
    # # @pytest.mark.flaky(rerun=6,rerun_delay=1)
    # def test_get_record_3(self, getHost):
    #     base_url = getHost + self.api + 'get_record'
    #     param = ['ndjs',121,'','&^^%$#$/*7',1.998,88888,None]
    #     params = {
    #         "page_no": random.choice(param),
    #         "video_type": random.choice(param),
    #         "_session": random.choice(param)
    #     }
    #     print("参数：",params)
    #     res = handle_request.run_main('GET',url = base_url,params=params,headers = self.headers)
    #     pytest.assume(res.status_code == 200)
    #     res = json.loads(res.text)
    #     pytest.assume(res["msg"] == 'Unauthorized' or 'Invalid app token')
    #
    #
