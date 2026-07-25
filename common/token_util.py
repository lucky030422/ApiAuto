from common.yaml_util import YamlUtil
from common.base_path import BASE_DIR

TOKEN_PATH = BASE_DIR / "extract" / "extract.yaml"


class TokenUtil:

    @staticmethod
    def save_token(token):
        YamlUtil.write_yaml(TOKEN_PATH, {"token": token})

    @staticmethod
    def get_token():
        data = YamlUtil.read_yaml(TOKEN_PATH)

        return data.get("token")

    @staticmethod
    def clear_token():
        YamlUtil.delete_yaml(TOKEN_PATH, "token")
