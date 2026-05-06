# testcases/test_login_ddt.py
import allure
import pytest
import requests
from config.settings import BASE_URL
from common.yaml_util import get_login_data

@allure.feature("登录模块")
class TestLoginDDT:
    @allure.story("登录接口数据驱动测试")
    @pytest.mark.parametrize("case", get_login_data())
    def test_login(self, case):
        with allure.step(f"准备测试数据: {case['name']}"):
            username = case["username"]
            password = case["password"]
            expected = case["expected_status"]

        with allure.step("发送登录请求"):
            resp = requests.post(
                f"{BASE_URL}/auth/login",
                json={"username": username, "password": password}
            )

        with allure.step("校验状态码"):
            assert resp.status_code == expected, f"用例 {case['name']} 失败"

        allure.attach(str(resp.json()), name="响应内容", attachment_type=allure.attachment_type.JSON)