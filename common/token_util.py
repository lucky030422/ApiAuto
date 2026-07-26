from common.yaml_util import YamlUtil
from common.base_path import BASE_DIR

# Token 持久化文件路径：extract/extract.yaml
TOKEN_PATH = BASE_DIR / "extract" / "extract.yaml"


class TokenUtil:
    """
    Token 管理器
    负责将登录获取的 token 持久化到 YAML 文件
    实现跨测试会话的 token 复用
    """

    @staticmethod
    def save_token(token):
        """保存 token 到 YAML 文件"""
        YamlUtil.write_yaml(TOKEN_PATH, {"token": token})

    @staticmethod
    def get_token():
        """从 YAML 文件读取 token"""
        data = YamlUtil.read_yaml(TOKEN_PATH)
        return data.get("token")

    @staticmethod
    def clear_token():
        """清除 YAML 文件中的 token"""
        YamlUtil.delete_yaml(TOKEN_PATH, "token")
