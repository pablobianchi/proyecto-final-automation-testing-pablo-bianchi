import pytest

from utils.helper import get_driver

@pytest.fixture
def driver():
    driver = get_driver();
    
    ##Idea clave
    ##return → devuelve y finaliza la función.
    ##yield → devuelve un valor y suspende la ejecución; la próxima iteración retoma donde quedó.
    yield driver
    driver.quit()