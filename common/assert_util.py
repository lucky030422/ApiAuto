from common.logger_util import LoggerUtil


class AssertUtil:

    @staticmethod
    def assert_resopnse(response, validate):
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
