import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

from utils.helper import USERNAME,PASSWORD, take_screenshot

@pytest.mark.ui
def test_inventory( driver ):


    loginPage = LoginPage( driver )
    loginPage.login_completo(USERNAME,PASSWORD)

    inventoryPage = InventoryPage( driver )
    

    take_screenshot(driver , 'inventario' );

    assert "Swag Labs" in inventoryPage.obtener_titulo() , f"Título inesperado: {inventoryPage.obtener_titulo()}"

    products = inventoryPage.obtener_productos()
    assert len(products) > 0 , f"No se encontraron productos"

    assert len( inventoryPage.obtener_elemento_orden() ) > 0  , f"No se encontró elemento de Orden"

    assert len( inventoryPage.obtener_menu_hamburguesa() ) > 0  , f"No se encontró elemento de Menú"

    
    
    