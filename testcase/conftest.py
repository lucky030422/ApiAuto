import pytest


@pytest.fixture(scope="session", autouse=True)
def login():
    """
    全局 session 级别的 login fixture
    autouse=True 表示所有测试用例自动使用此 fixture
    当前为占位实现，后续可在此完成登录操作并存储 token
    """
    print('login_session')
