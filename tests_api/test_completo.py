import pytest

import logging
import time
from faker import Faker
import pytest_check as check

logger = logging.getLogger("DEMO")  # __name__ = nombre del módulo

faker = Faker()

@pytest.mark.api
def test_get_users_ok(api_client):

    
    response = api_client("GET", "/users")
  
   
    assert response.status_code == 200, f"Status Code Incorrecto"
    #logger.debug("URL actual: %s", response.current_url)
    # más asserts sobre el JSON según tu caso


@pytest.mark.api
def test_completo(api_client, created_post):
    
    # utilizo directamete la que defini como modulo que me devuelve un response
    response = created_post
    
    # Validaciones CREATE
    assert response.status_code == 201, f"CREATE respondió {response.status_code}"
    
    # Validar headers
    assert 'application/json' in response.headers['Content-Type'], f"CREATE respondió {response.headers['Content-Type']}"
    assert 'charset=utf-8' in response.headers['Content-Type'], f"CREATE respondió {response.headers['Content-Type']}"
    
    # Validar performance
    assert response.elapsed.total_seconds() < 1, f"CREATE tardó {response.elapsed.total_seconds():.3f}s, supera 1s"
    
    created_post = response.json()
    post_id = created_post['id']    

    #print( post_id )

    

    #PATCH

    payload = {
        'title':  faker.text(50) ,
        'body': faker.text(5000),
        'userId': faker.random_digit()
    }
    
    response = api_client("PATCH", f'/posts/{post_id}', json=payload )
    # Validaciones PATCH
    assert response.status_code == 200, f"PATCH respondió {response.status_code}"
    
    # Validar headers
    assert 'application/json' in response.headers['Content-Type'], f"PATCH respondió {response.headers['Content-Type']}"
    assert 'charset=utf-8' in response.headers['Content-Type'], f"PATCH respondió {response.headers['Content-Type']}"
    
    # Validar performance
    check.is_true( response.elapsed.total_seconds() < 1, f"PATCH tardó {response.elapsed.total_seconds():.3f}s, supera 1s" )
      
    # Verificar que el título se actualizó
    updated_data = response.json()
    assert updated_data['title'] ==  payload['title'], f"El título no se actualizó, se envío {payload['title']} y respondió {updated_data['title']}"
    
    
    
    # DELETE 
    
    response = api_client("DELETE", f'/posts/{post_id}' )
    
    check.is_true( response.elapsed.total_seconds() < 1, f"DELETE tardó {response.elapsed.total_seconds():.3f}s, supera 1s" )

    #esto es así por que esta api devuelve 200, lo ideal sería 204 -> No Content
    assert response.status_code == 200, f"DELETE respondió {response.status_code}"
    
    
   