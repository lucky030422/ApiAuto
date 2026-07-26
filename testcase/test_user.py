# ============================================================
# 此文件已废弃，功能已迁移至 test_api.py 的数据驱动方式
# 保留注释代码供参考
# ============================================================

# import pytest
# from common.api_client import ApiClient
# from common.data_util import DataUtil
# from common.base_path import BASE_DIR
# cases=DataUtil.load_cases(BASE_DIR/'data'/'user.yaml')
# @pytest.mark.parametrize("case_name,case",cases)
# def test_user(case_name,case):
#     ApiClient.run(case)
