import pytest
import requests

from common.api_client import ApiClient
from common.data_util import DataUtil
from common.base_path import BASE_DIR


def load_all_cases():
    cases = []

    files = [
        "login.yaml",
        "user.yaml"
    ]
    for file in files:
        yaml_case = DataUtil.load_cases(BASE_DIR / "data" / file)

        cases.extend(yaml_case)
        cases.sort(key=lambda x:x[1].get("priority",999))
    return cases


cases = load_all_cases()



@pytest.mark.parametrize("case_name,case", cases, ids=[x[0] for x in cases])
def test_api(case_name, case):
    ApiClient.run(case)
