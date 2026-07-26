import allure
import json


class AllureUtil:
    """
    Allure 报告辅助工具类
    封装了向 Allure 报告附加文本和 JSON 数据的操作
    便于在测试报告中清晰地展示请求和响应信息
    """

    @staticmethod
    def attach_json(name, data):
        """
        将数据以 JSON 格式附加到 Allure 报告
        如果是 dict，先格式化为漂亮的 JSON 字符串再附加
        """
        if isinstance(data, dict):
            data = json.dumps(data, indent=4, ensure_ascii=False)
        allure.attach(data, name=name, attachment_type=allure.attachment_type.JSON)

    @staticmethod
    def attach_text(name, data):
        """将文本数据附加到 Allure 报告"""
        allure.attach(str(data), name=name, attachment_type=allure.attachment_type.TEXT)
