from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By  # Agregada esta línea
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def hacer_clic(driver, selector, timeout=10):
    try:
        elemento = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(selector))
        elemento.click()
        return True
    except:
        return False

def entrar(url):
    opciones = Options()
    opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
    opciones.add_experimental_option('useAutomationExtension', False)
    opciones.add_argument('--incognito')
    opciones.add_argument('--start-maximized')

    try:
        driver = webdriver.Chrome(options=opciones)
        driver.get(url)

        if not hacer_clic(driver, (By.ID, 'lnkCookie')):
            print('No se pudo hacer clic en el botón de cookies.')

        if hacer_clic(driver, (By.XPATH, '//*[@id="menuPrincipalRFEVB"]/div/ul/li[3]/a')):
            hacer_clic(driver, (By.XPATH, '//*[@id="miWrapper"]/ul/li[2]/ul/li[1]/a'))
            hacer_clic(driver, (By.XPATH, '//*[@id="miWrapper"]/ul/li[2]/ul/li[4]/a'))
            
        else:
            print('No se encontró la entrada correcta en competiciones.')
        return driver.get('https://www.rfevb.com/')
    
    except Exception as e:
        print(f"Error durante la navegación: {e}")
        