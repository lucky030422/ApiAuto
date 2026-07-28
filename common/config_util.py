import yaml
import os
from common.yaml_util import YamlUtil
from common.base_path import BASE_DIR

# 配置文件路径：config/config.yaml
CONFIG_PATH = BASE_DIR / "config" / "config.yaml"


class ConfigUtil:
    """
    配置工具类
    从 config/config.yaml 读取项目配置
    支持点号分隔的多级 key 访问，如 "base.url" 对应嵌套字典中的 base -> url
    """

    # # 类加载时一次性读取配置，全局共享
    # _config = YamlUtil.read_yaml(CONFIG_PATH)
    #
    # @classmethod
    # def get(cls, key):
    #     """
    #     根据点号分隔的 key 获取配置值
    #     示例:
    #         ConfigUtil.get("base.url")     -> "http://127.0.0.1:5000"
    #         ConfigUtil.get("timeout")      -> 10
    #         ConfigUtil.get("headers")      -> {"Content-Type": "application/json"}
    #     """
    #     data = cls._config
    #     keys = key.split(".")
    #
    #     for k in keys:
    #         data = data[k]
    #
    #     return data

    @classmethod
    def load(cls):
        env = os.getenv("TEST_ENV", "test")
        file = f"config/config-{env}.yaml"
        with open(file, encoding="utf-8") as f:
            return yaml.safe_load(f)

    @staticmethod
    def get(key):
        config = ConfigUtil.load()
        return config.get(key)
