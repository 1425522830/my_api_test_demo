# common/session_client.py
import requests
from config.settings import HEADERS
from tenacity import retry, stop_after_attempt, wait_fixed, retry_if_exception

def is_retryable(exception):
    # 判断异常对象是否属于requests类，排掉库本身的网络和请求问题
    if isinstance(exception, requests.exceptions.RequestException):
        return True
    # 检查异常对象是否有一个名为response的属性，排掉网络返回和服务层问题
    if hasattr(exception, 'response') and exception.response is not None:
        if 500 <= exception.response.status_code < 600:
            return True
    return False        # 4xx不重试

class SessionClient:
    def __init__(self, base_url=None):          # 支持实例化时可以传入基础URL
        self.base_url = base_url
        self.session = requests.Session()       # 自动保存cookies、重用相同的headers、以及复用底层的TCP连接
        self.update_headers(HEADERS)            # 合并请求头

    def _build_url(self, endpoint):             # 封装一个合并url的函数
        if self.base_url:
            return f"{self.base_url}{endpoint}"
        return endpoint

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2), retry=retry_if_exception(is_retryable))
    def post(self, endpoint, **kwargs):
        url = self._build_url(endpoint)
        return self.session.post(url, **kwargs)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2), retry=retry_if_exception(is_retryable))
    def get(self, endpoint, **kwargs):
        url = self._build_url(endpoint)
        return self.session.get(url, **kwargs)

    def set_header(self, key, value):
        self.session.headers[key] = value

    def update_headers(self, headers):
        self.session.headers.update(headers)