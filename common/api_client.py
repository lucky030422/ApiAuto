import allure
from common.request_util import RequestUtil
from common.extract_util import ExtractUtil
from common.assert_util import AssertUtil
from common.logger_util import LoggerUtil


class ApiClient:
    """
    API 客户端核心类
    编排单条接口测试用例的执行流程：
        1. 设置 Allure 报告标题
        2. 发送 HTTP 请求
        3. 附加响应数据到 Allure 报告
        4. 提取响应中的变量供后续用例使用
        5. 执行接口断言验证
    """

    @staticmethod
    def run(case):
        """
        执行一条接口测试用例

        参数:
            case: dict，测试用例数据，包含以下字段：
                - title:      用例标题（显示在 Allure 报告中）
                - request:    请求参数（method, url, headers, json 等）
                - extract:    变量提取规则（可选，JSONPath 表达式）
                - validate:   断言规则（可选，status_code/code/msg）
        """
        # 1. 设置 Allure 动态用例标题
        allure.dynamic.title(case.get('title'))

        # 2. 发送接口请求
        with allure.step('发送接口请求'):
            response = RequestUtil.send_request(**case["request"])

        # 3. 附件响应结果到 Allure 报告
        with allure.step("响应结果"):
            allure.attach(response.text, name='响应数据',
                          attachment_type=allure.attachment_type.JSON)

        # 4. 从响应中提取变量（如 token）
        with allure.step('提取变量'):
            ExtractUtil.extract(response, case.get("extract"))

        # 5. 执行接口断言
        with allure.step('接口断言'):
            AssertUtil.assert_resopnse(response, case.get("validate"))

        return response
