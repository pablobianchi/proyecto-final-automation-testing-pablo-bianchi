from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helper import URL

class CartPage:

    #ver si es necesario agregarle un /login o algo a la URL base
    URL = URL + "/cart.html"

    _PRODUCTOS = (By.CLASS_NAME, 'cart_item')
    _PRODUCTO_DETALLE = ( By.CLASS_NAME, 'inventory_item_name' )
    _ORDEN_SELECT = (By.CLASS_NAME, 'product_sort_container')
    _MENU_HAMBURGUESA = (By.CLASS_NAME, 'bm-burger-button')
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
    
    def obtener_nombre_producto(self,product_index=-1):
        
        products = self.obtener_productos()  
        product = None
        product_name = None

        if len( products ) > 0:

            if product_index >= 0:
                product = products[product_index]
            
                if( product is not None ):
                    product_name = product.find_element(*self._PRODUCTO_DETALLE ).get_attribute("innerHTML")

            return( product_name )
    
   
    def obtener_titulo( self ):

        return self.driver.title

    