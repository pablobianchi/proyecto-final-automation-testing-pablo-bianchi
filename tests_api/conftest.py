import pytest
import requests
import time
import logging
from utils.helper import logs_path

BASE = 'https://jsonplaceholder.typicode.com'

# Logger de este módulo
logger = logging.getLogger("API")

@pytest.fixture(scope='module')
def api_base_url():
    return f"{BASE}"

# @pytest.fixture(scope='module')
# def api_client(api_base_url):
#     def _client(method, path, **kwargs):
#         url = f"{api_base_url}{path}"
#         return requests.request(method, url, **kwargs)
#     return _client


#con logger incluido
@pytest.fixture(scope="module")
def api_client(api_base_url):
    def _client(method, path, **kwargs):
        url = f"{api_base_url}{path}"

        # Medimos el tiempo del request
        start = time.perf_counter()
        response = requests.request(method, url, **kwargs)
        duration = time.perf_counter() - start

        # Log: METHOD URL -> STATUS (X.XXX s)
        logger.info(
            "%s %s -> %s (%.3f s)",
            method.upper(),
            url,
            response.status_code,
            duration,
        )

        return response

    return _client

logging.basicConfig(
    level=logging.INFO,  # DEBUG / INFO / WARNING / ERROR
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(f"{logs_path}_log.log", "a", encoding="utf-8"),
        logging.StreamHandler()  # muestra también por consola
    ],
)

logger = logging.getLogger()