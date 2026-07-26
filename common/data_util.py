from common.yaml_util import YamlUtil


class DataUtil:
    """
    测试数据加载工具
    从 YAML 测试数据文件中加载用例
    每个 YAML 的顶层 key 作为用例名称，value 作为用例内容
    返回 (case_name, case_data) 元组的列表，供 pytest 参数化使用
    """

    @staticmethod
    def load_cases(path):
        """
        加载 YAML 测试用例文件
        返回格式：[("用例名1", {用例数据1}), ("用例名2", {用例数据2}), ...]
        """
        data = YamlUtil.read_yaml(path)
        return list(data.items())
