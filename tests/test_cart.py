import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.helper import USERNAME,PASSWORD, take_screenshot
import random
import time


def test_cart( driver ):


    loginPage = LoginPage( driver )
    loginPage.login_completo(USERNAME,PASSWORD)

    inventoryPage = InventoryPage( driver )
    take_screenshot(driver , 'inventario' )

    nombre_producto_agregado = ""

    # assert "Swag Labs" in inventoryPage.obtener_titulo() , f"Título inesperado: {inventoryPage.obtener_titulo()}"

    # products = inventoryPage.obtener_productos()
    # assert len(products) > 0 , f"No se encontraron productos"

    # product = random.choice(products)
    # #print(product.get_attribute("innerHTML"))

    # producto_added_name = product.find_element(By.CLASS_NAME, 'inventory_item_name').get_attribute("innerHTML") 
    nombre_producto_agregado = inventoryPage.agregar_producto(-1)
    assert nombre_producto_agregado != "" , f"No se agregó ningún producto"
    take_screenshot(driver , 'producto_agregado' )

    time.sleep(5)

    link_carrito = inventoryPage.obtener_link_carrito()
    assert link_carrito is not None , f"No se encontró el link del carrito"

    assert  inventoryPage.obtener_badge_carrito() is not None , f"No se encontró el Badge del carrito"


    if link_carrito is not None:

        link_carrito.click()
        time.sleep(3)
        cartPage = CartPage( driver )        
        assert cartPage.URL in driver.current_url, f"URL Incorrecta"
        take_screenshot(driver , 'carrito' )

        #TODO: Mejorar, habría que ir recorriendo el carrito y validar tambien en base al ultimo agregado

        productos_carrito = cartPage.obtener_productos()
        assert len(productos_carrito) > 0  , f"No hay productos en el carrito"

        assert nombre_producto_agregado == cartPage.obtener_nombre_producto(0)  , f"El Producto no es el agregado"


        #TODO: testear el remove
    