import requests

from common.config_util import ConfigUtil
from common.token_util import TokenUtil
from common.logger_util import LoggerUtil
from common.variable_util import VariableUtil
from common.allure_util import AllureUtil

class RequestUtil:

    @staticmethod
    def send_request(method,
                     url,
                     headers=None,
                     need_token=True,
                     **kwargs):
        base_url = ConfigUtil.get("base.url")
        timeout = ConfigUtil.get("timeout")

        if headers is None:
            headers = ConfigUtil.get("headers").copy()

        kwargs = VariableUtil.replace(kwargs)
        headers = VariableUtil.replace(headers)

        if need_token:
            token = VariableUtil.get("token")
            if token:
                headers["Authorization"] = f"Bearer {token}"

        full_url = f"{base_url.rstrip('/')}/{url.lstrip('/')}"

        LoggerUtil.info(f"请求方式:{method}")
        LoggerUtil.info(f"请求URL:{full_url}")
        LoggerUtil.info(f"请求参数:{kwargs}")
        LoggerUtil.info(f"请求头:{headers}")
        AllureUtil.attach_text("请求方式", method)
        AllureUtil.attach_text("请求url", full_url)
        AllureUtil.attach_json('请求参数',kwargs)

        try:
            response = requests.request(method=method,
                                        url=full_url,
                                        headers=headers,
                                        timeout=timeout,
                                        **kwargs)
            LoggerUtil.info(f"响应状态码:{response.status_code}")
            LoggerUtil.info(f"响应参数:{response.text}")
            AllureUtil.attach_json('响应数据',response.text)
            return response
        except Exception as e:
            LoggerUtil.error(str(e))
            raise RuntimeError(f"请求失败: {e}")
