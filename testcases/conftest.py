# testcases/conftest.py
import pytest
from common.session_client import SessionClient
from config.settings import BASE_URL, LOGIN_USERNAME, LOGIN_PASSWORD

@pytest.fixture(scope="session")
def api_client():
    """session 级别夹具：登录一次，返回带 token 的 SessionClient 实例"""
    client = SessionClient(base_url=BASE_URL)
    login_resp = client.post("/auth/login", json={
        "username": LOGIN_USERNAME,
        "password": LOGIN_PASSWORD
    })
    assert login_resp.status_code == 200, "登录失败"
    token = login_resp.json()["accessToken"]
    client.set_header("Authorization", f"Bearer {token}")
    return client