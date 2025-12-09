import pytest

import logging

logger = logging.getLogger("DEMO")  # __name__ = nombre del módulo

@pytest.mark.api
def test_get_users_ok(api_client):

    
    response = api_client("GET", "/users")
  
   
    assert response.status_code == 200, f"Status Code Incorrecto"
    #logger.debug("URL actual: %s", response.current_url)
    # más asserts sobre el JSON según tu caso