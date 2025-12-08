import pytest
from pages.login_page import LoginPage

from utils.helper import take_screenshot
from utils.datos import leer_csv_login

# Definimos nuestros casos de prueba

# CASOS_LOGIN = [
#  ("standard_user", "secret_sauce", True), # usuario válido, login exitoso
#  ("locked_out_user", "secret_sauce", False), # usuario bloqueado, login falla
#  ("usuario_malo", "password_malo", False), # credenciales inválidas, login falla
# ]

CASOS_LOGIN = leer_csv_login('data/data_login.csv')

# Ejemplo de uso

 # Resultado: [('standard_user', 'secret_sauce', True), ...]

@pytest.mark.parametrize("username,password,login_bool",CASOS_LOGIN)
@pytest.mark.ui
def test_login( driver, username , password , login_bool  ):

    loginPage = LoginPage( driver )

    loginPage.login_completo(username,password)
    
    

    take_screenshot(driver , 'login' )

    if login_bool:
        assert "inventory.html" in driver.current_url
    else:
        assert "inventory.html" not in driver.current_url

    
    