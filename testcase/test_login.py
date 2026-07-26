# ============================================================
# 此文件已废弃，功能已迁移至 test_api.py 的数据驱动方式
# 保留注释代码供参考
# ============================================================

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
#     cases=DataUtil.load_cases(BASE_DIR/"data"/"login.yaml")
#     @pytest.mark.parametrize("case_name,case",cases)
#     def test_case_login(self,case_name,case):
#         ApiClient.run(case)
