from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime
from pathlib import Path



REPORTS_FOLDER = 'reports'
TEST_VERSION = f"ejecucion_{datetime.now():%Y%m%d_%H%M%S}"

out = Path.cwd() / REPORTS_FOLDER / TEST_VERSION
out.mkdir(parents=True, exist_ok=True)


#base url del proyecto a testear, de aca se deberían desprender todas las demas URL
URL = 'https://www.saucedemo.com/'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'
BTNLOGIN = 'login-button'


##HELPER PARA CAPTURAR SCREENSHOOT
def take_screenshot( driver:webdriver.Chrome , nombre ):

    fname = f"{TEST_VERSION}_snap_{nombre}.png"
    driver.save_screenshot(str(out / fname))


def get_driver():

    # opciones del browser
    #options = Options
    #options.add_argument('--start-maximized');

    service = Service(ChromeDriverManager().install());
    driver = webdriver.Chrome(service=service)

    time.sleep(5)

    return driver


# def login( driver:webdriver.Chrome , screenshot=False ):

#     driver.get( URL )
#     ##TODO: validar url correcta y status code 200

   

#     driver.find_element( By.NAME, 'user-name').send_keys(USERNAME)
#     driver.find_element( By.NAME, 'password').send_keys(PASSWORD)

#     if screenshot:
#         take_screenshot(driver , 'login' );

#     driver.find_element( By.ID, BTNLOGIN).click()

#     time.sleep(7)