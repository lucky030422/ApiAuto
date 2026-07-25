# import pytest
# from common.data_util import DataUtil
# from common.base_path import BASE_DIR
# from common.request_util import RequestUtil
# from common.assert_util import AssertUtil
# from common.extract_util import ExtractUtil
# from common.api_client import ApiClient
#
# class TestLogin:
#
#     # def test_login(self):
#     #     code = 200
#     #     print('login')
#     #     assert code == 200
#     #
#     # def test_query(self):
#     #     text = "查询成功"
#     #     print('query')
#     #     assert text == "查询成功"
#     #
#     # def test_add(self):
#     #     text = "添加成功"
#     #     print('add')
#     #     assert text == "添加成功"
#
#     cases=DataUtil.load_cases(BASE_DIR/"data"/"login.yaml")
#     @pytest.mark.parametrize("case_name,case",cases)
#     def test_case_login(self,case_name,case):
#         ApiClient.run(case)
#
