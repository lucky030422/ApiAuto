import yaml


class YamlUtil:
    # 读
    @staticmethod
    def read_yaml(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    # 写
    @staticmethod
    def write_yaml(file_path, data):
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, allow_unicode=True)

    # 更新
    @staticmethod
    def update_yaml(file_path, key, value):
        data = YamlUtil.read_yaml(file_path)
        data[key] = value
        YamlUtil.write_yaml(file_path, data)

    # 删除
    @staticmethod
    def delete_yaml(file_path, key):
        data = YamlUtil.read_yaml(file_path)
        if key in data:
            del data[key]
        YamlUtil.write_yaml(file_path, data)
