import allure
import json


class AllureUtil:

    @staticmethod
    def attach_json(name, data):
        if isinstance(data, dict):
            data = json.dumps(data, indent=4, ensure_ascii=False)
        allure.attach(data, name=name, attachment_type=allure.attachment_type.JSON)

    @staticmethod
    def attach_text(name, data):
        allure.attach(str(data), name=name, attachment_type=allure.attachment_type.TEXT)
