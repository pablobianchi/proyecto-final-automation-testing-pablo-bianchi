from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helper import URL

class InventoryPage:

    #ver si es necesario agregarle un /login o algo a la URL base
    URL = URL + "/inventory.html"

    _PRODUCTOS = (By.CLASS_NAME, 'inventory_item')
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
    
    def obtener_elemento_orden(self):
        
        element = self.driver.find_elements(*self._ORDEN_SELECT)
        return element
    
    def obtener_menu_hamburguesa(self):
        
        element = self.driver.find_elements(*self._MENU_HAMBURGUESA)
        return element
   
    def obtener_titulo( self ):

        return self.driver.title

    