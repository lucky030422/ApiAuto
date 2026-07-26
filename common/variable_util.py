import re


class VariableUtil:
    """
    全局变量管理器
    提供变量的存储、获取和替换功能
    测试流程中提取的变量（如 token）通过此类管理，支持跨用例共享

    变量替换语法：${变量名}
    示例：请求参数中的 "Bearer ${token}" 会被替换为实际 token 值
    """

    # 类级别字典，全局共享变量存储
    _variables = {}

    @classmethod
    def set(cls, key, value):
        """存储变量"""
        cls._variables[key] = value

    @classmethod
    def get(cls, key):
        """获取变量值，不存在时返回 None"""
        return cls._variables.get(key)

    @classmethod
    def replace(cls, data):
        """
        递归替换数据结构中所有字符串值的 ${变量名} 占位符
        支持 dict、list 和 str 三种数据类型
        """
        if isinstance(data, dict):
            return {k: cls.replace(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [cls.replace(v) for v in data]
        elif isinstance(data, str):
            # 匹配 ${xxx} 格式的占位符
            pattern = r"\$\{(.*?)\}"

            def replace(match):
                key = match.group(1)
                return str(cls.get(key))

            return re.sub(pattern, replace, data)
        return data
