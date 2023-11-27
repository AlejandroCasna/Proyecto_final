
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from joblib import Parallel, delayed
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def hacer_clic(driver, selector, timeout=10):
    try:
        elemento = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(selector))
        elemento.click()
        return True
    except:
        return False

def scraping_libero(url):
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
            c = driver.find_element(By.CSS_SELECTOR, '#ctl00_Content_Main_ctl00_Content_Main_MainDivPanel').text.split('\n')
            print('Scraping exitoso')

        else:
            print('No se encontró la entrada correcta en competiciones.')
        return c
    
    except Exception as e:
        print(f"Error durante la navegación: {e}")

'''--------------------------------------------------------------------------------------------------------------------------------------------'''



def scraping_receptor(url):
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
            hacer_clic(driver,(By.XPATH, '//*[@id="ctl00_Content_Main_RLB_PlayerStats"]/div/ul/li[2]/a'))
            c = driver.find_element(By.CSS_SELECTOR, '#ctl00_Content_Main_ctl00_Content_Main_MainDivPanel').text.split('\n')
            print('Scraping exitoso')
        else:
            print('No se encontró la entrada correcta en competiciones.')
        return c
    
    except Exception as e:
        print(f"Error durante la navegación: {e}")
        


'''--------------------------------------------------------------------------------------------------------------------------------------------'''



def scraping_central(url):
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
            hacer_clic(driver,(By.XPATH, '//*[@id="ctl00_Content_Main_RLB_PlayerStats"]/div/ul/li[4]/a'))
            c = driver.find_element(By.CSS_SELECTOR, '#ctl00_Content_Main_ctl00_Content_Main_MainDivPanel').text.split('\n')
            print('Scraping exitoso')
        else:
            print('No se encontró la entrada correcta en competiciones.')
        return c
    
    except Exception as e:
        print(f"Error durante la navegación: {e}")

'''--------------------------------------------------------------------------------------------------------------------------------------------'''

def scraping_colocador(url):
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
            hacer_clic(driver,(By.XPATH, '//*[@id="ctl00_Content_Main_RLB_PlayerStats"]/div/ul/li[5]/a'))
            c = driver.find_element(By.CSS_SELECTOR, '#ctl00_Content_Main_ctl00_Content_Main_MainDivPanel').text.split('\n')
            print('Scraping exitoso')
        else:
            print('No se encontró la entrada correcta en competiciones.')
        return c
    
    except Exception as e:
        print(f"Error durante la navegación: {e}")

'''--------------------------------------------------------------------------------------------------------------------------------------------'''


def scraping_opuesto(url):
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
            hacer_clic(driver,(By.XPATH, '//*[@id="ctl00_Content_Main_RLB_PlayerStats"]/div/ul/li[3]/a'))
            c = driver.find_element(By.CSS_SELECTOR, '#ctl00_Content_Main_ctl00_Content_Main_MainDivPanel').text.split('\n')
            print('Scraping exitoso')
        else:
            print('No se encontró la entrada correcta en competiciones.')
        return c
    
    except Exception as e:
        print(f"Error durante la navegación: {e}")       


'''--------------------------------------------------------------------------------------------------------------------------------------------'''
def scraping_equipos(url):
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
            hacer_clic(driver, (By.XPATH , '//*[@id="miWrapper"]/ul/li[2]/ul/li[1]/a'))
            hacer_clic(driver,(By.XPATH, '//*[@id="ctl00_Content_Main_RLB_PlayerStats"]/div/ul/li[3]/a'))
            equipos = driver.find_elements(By.CLASS_NAME, 'rlvI')[0:12]

            datos = []
            for i in range(len(equipos)):
                e = driver.find_elements(By.CLASS_NAME, 'rlvI')[i]
                nombre_equipo = e.text  
                print(nombre_equipo)  
                e.click()
                print('Estoy dentro.')
                time.sleep(1)
                datos.append(nombre_equipo)
                driver.get('https://rfevb-web.dataproject.com/CompetitionTeamSearch.aspx?ID=124')
            
            print('Scraping exitoso')
        else:
            print('No se encontró la entrada correcta en competiciones.')
        return datos
    
    except Exception as e:
        print(f"Error durante la navegación: {e}")  



'''--------------------------------------------------------------------------------------------------------------------------------------'''

def scraping_jugadores(url):
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
            hacer_clic(driver, (By.XPATH , '//*[@id="miWrapper"]/ul/li[2]/ul/li[1]/a'))
            hacer_clic(driver,(By.XPATH, '//*[@id="ctl00_Content_Main_RLB_PlayerStats"]/div/ul/li[3]/a'))
            equipos = driver.find_elements(By.CLASS_NAME, 'rlvI')[0:12]

            superLiga_Masculino=[]
            for i in range(12):
                
                e = driver.find_elements(By.CLASS_NAME, 'rlvI')[i]
                
                print(e.text)
                
                e.click()
                
                print('Estoy dentro.')
                
                time.sleep(1)
            
                superLiga_Masculino.append(driver.find_elements(By.CLASS_NAME , 't-row')[3].text.split('\n'))
                
                print('Extraigo')
                
                time.sleep(1)
                
                driver.get('https://rfevb-web.dataproject.com/CompetitionTeamSearch.aspx?ID=124')
                
                time.sleep(1)
            print('Scraping exitoso')
        else:
            print('No se encontró la entrada correcta en competiciones.')
        return superLiga_Masculino
    
    except Exception as e:
        print(f"Error durante la navegación: {e}")
