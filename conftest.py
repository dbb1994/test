import pytest
import yaml

yml_file = '/Users/wangjin/PycharmProjects/apiauto/config/host.yml'

@pytest.fixture()
def getHost():
    with open(yml_file, 'r') as f:
        yml_data = yaml.safe_load(f)
        host = yml_data.get("host").get("test1")
        print(host)
    return host

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
