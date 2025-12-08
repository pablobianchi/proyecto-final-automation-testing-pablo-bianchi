import pytest
import pytest_html

from utils.helper import get_driver,out
from py.xml import html

import base64


@pytest.fixture
def driver():
    driver = get_driver();
    
    ##Idea clave
    ##return → devuelve y finaliza la función.
    ##yield → devuelve un valor y suspende la ejecución; la próxima iteración retoma donde quedó.
    yield driver
    driver.quit()



def pytest_html_report_title(report):
    """Cambia el título de la pestaña del navegador"""
    report.title = "TalentoLab – Reporte de Testing"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook que se ejecuta después de cada fase del test.
    Lo usamos para enganchar la URL actual (Selenium) en el 'report'.
    """
    outcome = yield
    report = outcome.get_result()

    # Solo nos interesa la fase de "call" (cuando se ejecuta el cuerpo del test)
    if call.when == "call":
        # Si el test usa la fixture 'driver', la encontrás en item.funcargs
        driver = item.funcargs.get("driver")
        if driver is not None:
            # Le agregamos un atributo custom al reporte
            report.url = getattr(driver, "current_url", "")

    if report.when == 'call' and report.failed:
        driver = item.funcargs.get('driver') # Obtenemos elfixture driver
        if driver:
            file_name = out / f"{item.name}.png"
            driver.save_screenshot(str(file_name)) # 📸¡Captura!

            #GPT
            # Adjuntamos la captura como extra en el reporte HTML
            # Usamos base64 para que funcione bien con --self-contained-html
            png_bytes_b64 = driver.get_screenshot_as_base64()

            # HTML: imagen + link clickeable que abre en otra pestaña
            html = (
                f'<a href="data:image/png;base64,{png_bytes_b64}" target="_blank">'
                f'<img src="data:image/png;base64,{png_bytes_b64}" '
                'style="max-width: 400px; border: 1px solid #ccc;" />'
                '</a>'
            )

            report.extras = getattr(report, "extras", [])
            report.extras.append(pytest_html.extras.html(html))
            # report.extras.append(
            #     extras.png(
            #         png_bytes_b64,
            #         name=f"Screenshot - {item.name}",
            #     )
            # )   



#refinada con GPT
def pytest_html_results_table_header(cells):
    """
    Agregamos una columna 'URL' en el header de la tabla del reporte.
    """
    if html is None:
        return
    # Por ejemplo, en la segunda posición (índice 1 o 2 según gustos)
    cells.insert(2, html.th("URL"))

#refinada con GPT
def pytest_html_results_table_row(report, cells):
    """
    Pintamos la URL en la fila correspondiente al test.
    """
    if html is None:
        return
    url = getattr(report, "url", "")
    cells.insert(2, html.td(url))