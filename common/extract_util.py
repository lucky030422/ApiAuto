from jsonpath import jsonpath

from common.variable_util import VariableUtil
from common.logger_util import LoggerUtil


class ExtractUtil:
    """
    响应数据提取工具类
    使用 JSONPath 表达式从接口响应中提取数据
    提取结果存入 VariableUtil 全局变量，供后续用例使用
    """

    @staticmethod
    def extract(response, extract_data):
        """
        提取接口响应中的数据

        参数:
            response: requests.Response 对象（接口响应）
            extract_data: dict，格式如 {"变量名": {"jsonpath": "$.data.token"}}

        提取结果通过 VariableUtil.set() 存储
        """
        if not extract_data:
            return

        body = response.json()

        for key, value in extract_data.items():
            json_path = value["jsonpath"]

            result = jsonpath(body, json_path)
            if result:
                VariableUtil.set(key, result[0])
                LoggerUtil.info(f"提取变量:{key}，值:{result[0]}")
