import yaml


class YamlUtil:
    """
    YAML 文件读写工具类
    提供对 YAML 文件的读取、写入、更新和删除操作
    作为数据持久化和配置管理的基础组件
    """

    @staticmethod
    def read_yaml(file_path):
        """读取 YAML 文件，返回 Python 对象（dict/list）"""
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    @staticmethod
    def write_yaml(file_path, data):
        """将数据写入 YAML 文件（覆盖写）"""
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, allow_unicode=True)

    @staticmethod
    def update_yaml(file_path, key, value):
        """更新 YAML 文件中指定 key 的值，其他内容保持不变"""
        data = YamlUtil.read_yaml(file_path)
        data[key] = value
        YamlUtil.write_yaml(file_path, data)

    @staticmethod
    def delete_yaml(file_path, key):
        """删除 YAML 文件中指定的 key"""
        data = YamlUtil.read_yaml(file_path)
        if key in data:
            del data[key]
        YamlUtil.write_yaml(file_path, data)
