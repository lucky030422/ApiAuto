from jsonpath import jsonpath

from common.variable_util import VariableUtil
from common.logger_util import LoggerUtil


class ExtractUtil:

    @staticmethod
    def extract(response, extract_data):
        if not extract_data:
            return

        body = response.json()

        for key, value in extract_data.items():
            json_path = value["jsonpath"]

            result = jsonpath(body, json_path)
            if result:
                VariableUtil.set(key, result[0])
                LoggerUtil.info(f"提取变量:{key}，值:{result[0]}")
