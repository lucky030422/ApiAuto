from common.yaml_util import YamlUtil


class DataUtil:

    @staticmethod
    def load_cases(path):
        data = YamlUtil.read_yaml(path)

        return list(data.items())
