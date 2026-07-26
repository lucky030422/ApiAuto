from common.logger_util import LoggerUtil


class AssertUtil:
    """
    断言工具类
    提供接口响应结果的通用断言方法
    支持对响应状态码、业务 code、业务 msg 的验证
    """

    @staticmethod
    def assert_resopnse(response, validate):
        """
        执行接口响应断言

        参数:
            response: requests.Response 对象
            validate: dict，断言规则，支持以下 key:
                - status_code: 验证 HTTP 状态码
                - code: 验证响应 JSON 中的业务 code
                - msg: 验证响应 JSON 中的业务 msg

        示例 validate:
            {"status_code": 200, "code": 200, "msg": "success"}
        """
        try:
            body = response.json()
        except Exception:
            raise AssertionError(f"响应数据不是json格式,状态码{response.status_code},响应内容{response.text}")

        if "status_code" in validate:
            assert response.status_code == validate[
                'status_code'], f"状态码断言失败,Excepted:{validate['status_code']},Actual:{response.status_code}"
            LoggerUtil.info(f"状态码断言成功,Excepted:{validate['status_code']},Actual:{response.status_code}")
        if "code" in validate:
            assert body.get("code") == validate["code"]
        if "msg" in validate:
            assert body.get("msg") == validate["msg"]
