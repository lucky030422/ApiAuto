import re


class VariableUtil:
    _variables = {}

    @classmethod
    def set(cls, key, value):
        cls._variables[key] = value

    @classmethod
    def get(cls, key):
        return cls._variables.get(key)

    @classmethod
    def replace(cls, data):
        if isinstance(data,dict):
            return {k: cls.replace(v) for k, v in data.items()}
        elif isinstance(data,list):
            return [cls.replace(v) for v in data]
        elif isinstance(data,str):
            pattern=r"\$\{(.*?)\}"
            def replace(match):
                key=match.group(1)

                return str(cls.get(key))
            return re.sub(pattern,replace,data)
        return data


