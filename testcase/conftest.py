import pytest


@pytest.fixture(scope="session",autouse=True)
def login():
    print('login_session')