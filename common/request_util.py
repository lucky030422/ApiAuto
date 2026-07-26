import requests

from common.config_util import ConfigUtil
from common.token_util import TokenUtil
from common.logger_util import LoggerUtil
from common.variable_util import VariableUtil
from common.allure_util import AllureUtil


class RequestUtil:
    """
    HTTP 请求工具类
    封装 requests 库，统一处理：
        - 基础 URL 拼接
        - 请求头配置（含 Authorization token）
        - 变量替换（${变量名} 占位符）
        - 请求/响应日志记录
        - Allure 报告附加请求信息
        - 超时和异常处理
    """

    @staticmethod
    def send_request(method,
                     url,
                     headers=None,
                     need_token=True,
                     **kwargs):
        """
        发送 HTTP 请求

        参数:
            method:     请求方法（GET/POST/PUT/DELETE 等）
            url:        接口路径（与 base url 拼接为完整 URL）
            headers:    请求头（可选，默认使用配置中的全局 headers）
            need_token: 是否自动添加 Authorization Bearer token
            **kwargs:   requests.request 的其他参数（json, params, data 等）

        返回:
            requests.Response 对象
        """
        # 从配置读取基础参数
        base_url = ConfigUtil.get("base.url")
        timeout = ConfigUtil.get("timeout")

        # 默认使用全局配置的请求头
        if headers is None:
            headers = ConfigUtil.get("headers").copy()

        # 变量替换：将 ${变量名} 替换为实际值
        kwargs = VariableUtil.replace(kwargs)
        headers = VariableUtil.replace(headers)

        # 自动添加 Bearer token
        if need_token:
            token = VariableUtil.get("token")
            if token:
                headers["Authorization"] = f"Bearer {token}"

        # 拼接完整 URL
        full_url = f"{base_url.rstrip('/')}/{url.lstrip('/')}"

        # 控制台日志输出
        LoggerUtil.info(f"请求方式:{method}")
        LoggerUtil.info(f"请求URL:{full_url}")
        LoggerUtil.info(f"请求参数:{kwargs}")
        LoggerUtil.info(f"请求头:{headers}")

        # Allure 报告附加请求信息
        AllureUtil.attach_text("请求方式", method)
        AllureUtil.attach_text("请求url", full_url)
        AllureUtil.attach_json('请求参数', kwargs)

        try:
            # 发送 HTTP 请求
            response = requests.request(method=method,
                                        url=full_url,
                                        headers=headers,
                                        timeout=timeout,
                                        **kwargs)
            # 响应日志
            LoggerUtil.info(f"响应状态码:{response.status_code}")
            LoggerUtil.info(f"响应参数:{response.text}")
            AllureUtil.attach_json('响应数据', response.text)
            return response
        except Exception as e:
            LoggerUtil.error(str(e))
            raise RuntimeError(f"请求失败: {e}")
