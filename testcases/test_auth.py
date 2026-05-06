# testcases/test_auth.py
from config.settings import LOGIN_USERNAME

def test_get_user_info(api_client):
    """测试获取当前用户信息"""
    resp = api_client.get("/auth/me")
    assert resp.status_code == 200
    assert resp.json()["username"] == LOGIN_USERNAME

def test_get_cart(api_client):
    """测试获取购物车"""
    resp = api_client.get("/carts/user/1")
    assert resp.status_code == 200
    assert "carts" in resp.json()