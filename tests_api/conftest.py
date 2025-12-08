import pytest
import requests


BASE = 'https://jsonplaceholder.typicode.com'

@pytest.fixture(scope='module')
def api_base_url():
    return f"{BASE}"

@pytest.fixture(scope='module')
def api_client(api_base_url):
    def _client(method, path, **kwargs):
        url = f"{api_base_url}{path}"
        return requests.request(method, url, **kwargs)
    return _client