import pytest

@pytest.mark.api
def test_get_users_ok(api_client):
    response = api_client("GET", "/users")
    print( response.json() )
    assert response.status_code == 200, f"Status Code Incorrecto"
    # más asserts sobre el JSON según tu caso