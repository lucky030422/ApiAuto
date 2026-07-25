import allure
from common.request_util import RequestUtil
from common.extract_util import ExtractUtil
from common.assert_util import AssertUtil
from common.logger_util import LoggerUtil


class ApiClient:

    @staticmethod
    def run(case):
        allure.dynamic.title(case.get('title'))
        with allure.step('发送接口请求'):
            response = RequestUtil.send_request(**case["request"])
        with allure.step("响应结果"):
            allure.attach(response.text, name='响应数据',
                          attachment_type=allure.attachment_type.JSON)
        with allure.step('提取变量'):
            ExtractUtil.extract(response, case.get("extract"))
        with allure.step('接口断言'):
            AssertUtil.assert_resopnse(response, case.get("validate"))


        return response
