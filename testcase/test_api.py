import pytest
import requests

from common.api_client import ApiClient
from common.data_util import DataUtil
from common.base_path import BASE_DIR


def load_all_cases():
    """
    加载所有 YAML 测试数据文件中的用例
    支持多文件合并，并按 priority（优先级）字段排序

    返回:
        [(case_name, case_data), ...] 格式的用例列表
    """
    cases = []

    # 需要加载的 YAML 测试数据文件列表
    files = [
        "login.yaml",
        "user.yaml"
    ]
    for file in files:
        yaml_case = DataUtil.load_cases(BASE_DIR / "data" / file)
        cases.extend(yaml_case)
        # 按优先级排序，priority 值越小越先执行
        cases.sort(key=lambda x: x[1].get("priority", 999))
    return cases


# 预加载所有测试用例（模块加载时执行）
cases = load_all_cases()


@pytest.mark.parametrize("case_name,case", cases, ids=[x[0] for x in cases])
def test_api(case_name, case):
    """
    数据驱动的主测试函数
    通过 pytest 参数化，将 YAML 中的每条用例自动生成一个测试用例

    参数:
        case_name: 用例名称（来自 YAML 的顶层 key）
        case:      用例数据字典（包含 request/validate/extract 等字段）
    """
    ApiClient.run(case)
