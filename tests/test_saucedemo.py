import pytest

from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import time
##para poder utilizar lo que definí dentro de utils
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from pages.login_page import LoginPage

from utils.helper import get_driver,take_screenshot,USERNAME,PASSWORD

# @pytest.fixture
# def driver():
#     driver = get_driver();
    
#     ##Idea clave
#     ##return → devuelve y finaliza la función.
#     ##yield → devuelve un valor y suspende la ejecución; la próxima iteración retoma donde quedó.
#     yield driver
#     driver.quit()




# def test_login( driver ):
#     login(driver,True)
#     assert "/inventory.html" in driver.current_url


# def test_inventory(driver:webdriver.Chrome  ):

#     loginPage = LoginPage( driver )
#     loginPage.login_completo(USERNAME,PASSWORD)

#     take_screenshot(driver , 'inventario' );

#     assert "Swag Labs" in driver.title , f"Título inesperado: {driver.title}"

#     products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
#     assert len(products) > 0 , f"No se encontraron productos"

#     assert len( driver.find_elements(By.CLASS_NAME, 'product_sort_container' ) ) > 0  , f"No se encontró elemento de Orden"

#     assert len( driver.find_elements(By.CLASS_NAME, 'bm-burger-button' ) ) > 0  , f"No se encontró elemento de Menú"


def test_carrito( driver:webdriver.Chrome  ):

    loginPage = LoginPage( driver )
    loginPage.login_completo(USERNAME,PASSWORD)
    take_screenshot(driver , 'inventario' )

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0 , f"No se encontraron productos"

    product = random.choice(products)
    #print(product.get_attribute("innerHTML"))

    producto_added_name = product.find_element(By.CLASS_NAME, 'inventory_item_name').get_attribute("innerHTML") 
   
    btn_agregar = product.find_element(By.CLASS_NAME, 'btn_inventory')
    assert btn_agregar is not None , f"No se encontró el botón para agregar"
    
    btn_agregar.click()

    time.sleep(2)

    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert badge is not None , f"No se marcó el Producto en el carrito"

    take_screenshot(driver , 'producto_agregado' )

    time.sleep(2)

    link = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    assert link is not None , f"No se el link del carrito"

    link.click()
    time.sleep(5)
    take_screenshot(driver , 'carrito' )
    assert "/cart.html" in driver.current_url, f"No es la pagina correcta del Carrito"

    #TODO: Mejorar, habría que ir recorriendo el carrito

    productos_carrito = driver.find_elements(By.CLASS_NAME, 'cart_item')
    assert len(productos_carrito) > 0  , f"No hay productos en el carrito"

    assert productos_carrito[0].find_element(By.CLASS_NAME, 'inventory_item_name').get_attribute("innerHTML") == producto_added_name  , f"El Producto no es el agregado"


