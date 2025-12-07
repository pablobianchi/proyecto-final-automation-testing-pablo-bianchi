from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helper import URL

import random;

class InventoryPage:

    #ver si es necesario agregarle un /login o algo a la URL base
    URL = URL + "/inventory.html"

    _PRODUCTOS = (By.CLASS_NAME, 'inventory_item')
    _ORDEN_SELECT = (By.CLASS_NAME, 'product_sort_container')
    _MENU_HAMBURGUESA = (By.CLASS_NAME, 'bm-burger-button')
    _PRODUCT_ADD_BUTTON = (By.CLASS_NAME, 'btn_inventory')
    _PRODUCT_DETALLE = (By.CLASS_NAME, 'inventory_item_name')
    _CARRITO_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    _CARRITO_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    #_ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)
        return self

    def obtener_productos(self):
        
        products = self.driver.find_elements(*self._PRODUCTOS)
        return products
    
    def agregar_producto(self,product_index=-1):
        
        products = self.obtener_productos()
        product_added_name = ""
        product = None

        if len( products ) > 0:

            if product_index == -1:
                product = random.choice(products)
            elif  product_index < len(products):
                product = products[product_index]

            if( product is not None ):

                btnAgregar = product.find_element(*self._PRODUCT_ADD_BUTTON)
                if btnAgregar is not None:
                    btnAgregar.click()
                    product_added_name = product.find_element(*self._PRODUCT_DETALLE ).get_attribute("innerHTML")

            return( product_added_name )
   
    
    def obtener_elemento_orden(self):
        
        element = self.driver.find_elements(*self._ORDEN_SELECT)
        return element
    
    def obtener_menu_hamburguesa(self):
        
        element = self.driver.find_elements(*self._MENU_HAMBURGUESA)
        return element
   
    def obtener_titulo( self ):

        return self.driver.title
    
    def obtener_link_carrito( self ):

        try:
            return self.driver.find_element(*self._CARRITO_LINK)
        except:
            return None


    def obtener_badge_carrito( self ):

        try:
            return self.driver.find_element(*self._CARRITO_BADGE)
        except:
            return None
