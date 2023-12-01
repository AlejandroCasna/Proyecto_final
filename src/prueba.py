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
import difflib
from sqlalchemy import create_engine, text, Integer
import re
import warnings
from selenium.common.exceptions import NoSuchElementException

warnings.filterwarnings("ignore")

def hacer_clic(driver, by_locator):
    try:
        driver.find_element(*by_locator).click()
        
    except NoSuchElementException:
        print('hola')
    except Exception as e:
        print(f"Error al hacer clic: {e}")
        

def scraping(url, parametro='jugadores'):

    ''' Obligatoriamente pasar URL.
            Parametro por defecto Jugadores.


            Parametros opcionales: 
            Equipo.
            Estadistica_jugador.
            Estadistica_equipo.
            Clasificacion.
            Jugadores.


            los parametros son tipo str.
    '''
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
    except Exception as e:
        print(f"Error durante la navegación: {e}")
        
    superLiga_Masculino = []  
    if parametro == 'jugadores':
        equipos = driver.find_elements(By.CLASS_NAME, 'rlvI')[0:12]
        for i in range(12):
            e = equipos[i]
            print(e.text)
            e.click()
            print('Estoy dentro.')
            time.sleep(1)
            superLiga_Masculino.append(driver.find_elements(By.CLASS_NAME, 't-row')[3].text.split('\n'))
            print('Extraigo')
            time.sleep(1)
            driver.get('https://rfevb-web.dataproject.com/CompetitionTeamSearch.aspx?ID=124')
            time.sleep(1)
        print('Scraping exitoso')

    elif parametro == 'equipo':
        equipos = driver.find_elements(By.CLASS_NAME, 'rlvI')[0:12]
        datos = []
        for i in range(len(equipos)):
            e = equipos[i]
            nombre_equipo = e.text
            print(nombre_equipo)
            e.click()
            print('Estoy dentro.')
            time.sleep(1)
            datos.append(nombre_equipo)
            driver.get('https://rfevb-web.dataproject.com/CompetitionTeamSearch.aspx?ID=124')
            time.sleep(1)
        print('Scraping exitoso')
        return datos

    elif parametro == 'estadistica_jugador':
        datos_por_pagina = {}
        for i in range(1, 6):
            hacer_clic(driver, (By.XPATH, f'//*[@id="ctl00_Content_Main_RLB_PlayerStats"]/div/ul/li[{i}]/a'))
            time.sleep(2)

            datos_pagina_actual = []

            try:
                datos_pagina_actual = driver.find_element(By.CSS_SELECTOR, '#RG_PlayerRanking_Libero').text.split('\n')
            except:
                pass

            if not datos_pagina_actual:
                try:
                    datos_pagina_actual = driver.find_element(By.CSS_SELECTOR, '#RG_PlayerRanking_Wingspiker_m').text.split('\n')
                except:
                    pass

            if not datos_pagina_actual:
                try:
                    datos_pagina_actual = driver.find_element(By.CSS_SELECTOR, '#RG_PlayerRanking_Opposite').text.split('\n')
                except:
                    pass

            if not datos_pagina_actual:
                try:
                    datos_pagina_actual = driver.find_element(By.CSS_SELECTOR, '#RG_PlayerRanking_MiddleBlocker_m').text.split('\n')
                except:
                    pass

            if not datos_pagina_actual:
                try:
                    datos_pagina_actual = driver.find_element(By.CSS_SELECTOR, '#RG_PlayerRanking_Setter').text.split('\n')
                except:
                    pass

            datos_por_pagina[i] = datos_pagina_actual
            driver.back()
            time.sleep(2)
            driver.get('https://rfevb-web.dataproject.com/Statistics.aspx?ID=111&PID=137')

        print('Scraping exitoso')
        return datos_por_pagina

    elif parametro == 'clasificacion':
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#tournament-table-tabs-and-content'))
        )
        clas = driver.find_element(By.CSS_SELECTOR, '#tournament-table-tabs-and-content').text.split('\n')
        print('Scraping exitoso')
        return clas

    elif parametro == 'estadistica_equipo':
        hacer_clic(driver, (By.XPATH, '//*[@id="RTS_Statistics_StatsType"]/div/ul/li[2]/a/span/span/span'))
        time.sleep(2)
        clas = driver.find_element(By.CSS_SELECTOR, '#RG_Stats_Recap').text.split('\n')
        print('Scraping exitoso')
        return clas
    else:
        print('algo anda mal')





