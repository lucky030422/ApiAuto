from common.yaml_util import YamlUtil
from common.base_path import BASE_DIR

CONFIG_PATH = BASE_DIR / "config" / "config.yaml"


class ConfigUtil:

    _config=YamlUtil.read_yaml(CONFIG_PATH)

    @classmethod
    def get(cls,key):

        data= cls._config
        keys=key.split(".")

        for k in keys:
            data=data[k]

        return data