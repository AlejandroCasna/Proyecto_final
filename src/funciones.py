
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
from fuzzywuzzy import process
import difflib
from sqlalchemy import create_engine ,text , Integer
import re
from unidecode import unidecode




opciones = Options()
opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_experimental_option('useAutomationExtension', False)
opciones.add_argument('--incognito')
opciones.add_argument('--start-maximized')










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



'''--------------------------------------------------------------------------------------------------------------------------------------'''

def scraping_jornadas(url):
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
            hacer_clic(driver, (By.XPATH, '//*[@id="miWrapper"]/ul/li[1]/ul/li[1]/a'))
            hacer_clic(driver, (By.XPATH, '//*[@id="jornadas"]'))
            hacer_clic(driver, (By.XPATH, '//*[@id="jornadas"]/option[1]'))
            time.sleep(5)
            data = driver.find_element(By.XPATH, '//*[@id="CPContenido_rptPlugins_PanPlugin_0"]/div').text.split('\n')[52:]

            jornadas = []
            for i in data:
                if 'JORNADA' in i:
                    temp = []
                    temp.append(i)
                    jornadas.append(temp)
                else:
                    temp.append(i)

            dataframes_por_jornada = {}

            for jornada in jornadas:
                fechas = []
                horas = []
                enfrentamientos = []

                for i in range(1, len(jornada), 4):
                    fecha = jornada[i + 1]
                    hora = jornada[i + 2]
                    enfrentamiento = jornada[i + 3]

                    fechas.append(fecha)
                    horas.append(hora)
                    enfrentamientos.append(enfrentamiento)

                df = pd.DataFrame({'fecha': fechas, 'hora': horas, 'enfrentamiento': enfrentamientos})

                num_jornada = int(jornada[0].split()[-1])

                dataframes_por_jornada[num_jornada] = df

            
            df_final = pd.concat(dataframes_por_jornada.values(), ignore_index=True)

            print('Scraping exitoso')
            return df_final

        else:
            print('No se encontró la entrada correcta en competiciones.')
            

    except Exception as e:
        print(f"Error durante la navegación: {e}")

'''--------------------------------------------------------------------------------------------------------------------------------------'''



def scraping_estadistica(url):

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
            hacer_clic(driver, (By.XPATH, '//*[@id="RTS_Statistics_StatsType"]/div/ul/li[2]/a/span/span'))
            time.sleep(5)
            clas = driver.find_element(By.CSS_SELECTOR, '#printableArea').text.split('\n')
            print('Scraping exitoso')
            return clas

    except Exception as e:
        print(f"Error durante la navegación: {e}")
    else:
        print('No se encontró la entrada correcta en competiciones.')
    finally:
        if driver:
            driver.quit()


'''--------------------------------------------------------------------------------------------------------------------------------------'''

def equipos(df):

    
    mapeo = {
        'Arenal Emevé': 'Arenal Emevé',
        'Barça Voleibol': 'Barça Voleibol',
        'Club Vóley Palma': 'Voley Palma',
        'Conectabalear CV Manacor': 'Manacor',
        'CV Guaguas': 'Guaguas',
        'Léleman Conqueridor Valencia': 'Conqueridor Valencia',
        'Melilla Sport Capital': 'CV Melilla',
        'Pamesa Teruel Voleibol': 'CV Teruel',
        'Rio Duero Soria': 'Rio Duero Soria',
        'Rotogal Boiro': 'Rotogal Boiro',
        'Unicaja Costa de Almeria': 'Unicaja Almería',
        'Voley Textil Santanderina': 'Voley Textil Santanderina'
    }
    df['Equipo'] = df['Equipo'].map(mapeo)

    return df

'''--------------------------------------------------------------------------------------------------------------------------------------'''
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def hacer_clic(driver, by_locator):
    try:
        driver.find_element(*by_locator).click()
        return True
    except:
        return False

def scraping(url, parametro='jugadores'):
    ''' Obligatoriamente pasar URL.

        Parametro por defecto Jugadores.
        Parametros opcionales: 
        Equipo
        Estadistica
        Clasificacion_jugador.
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
            return None

    except Exception as e:
        print(f"Error durante la navegación: {e}")
        return None

    superLiga_Masculino = []  # Inicializar la lista al principio

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

    elif parametro == 'estadistica':
        lista = []
        for i in range(5):
            hacer_clic(driver, (f'//*[@id="ctl00_Content_Main_RLB_PlayerStats"]/div/ul/li[{i}]/a'))
            c = driver.find_element(By.CSS_SELECTOR, '#ctl00_Content_Main_ctl00_Content_Main_MainDivPanel').text.split('\n')
            lista.append(c)
            driver.get(url)
            print('Scraping exitoso')
        return lista

    elif parametro == 'clasificacion_jugador':
        driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        clas = driver.find_element(By.CSS_SELECTOR, '#tournament-table-tabs-and-content').text.split('\n')
        print('Scraping exitoso')
        return clas

    try:
        driver = webdriver.Chrome(options=opciones)
        driver.get(url)
    except:
        pass

    for i in range(1, 5):
        datos_por_pagina = {}
        hacer_clic(driver, (By.XPATH, f'//*[@id="ctl00_Content_Main_RLB_PlayerStats"]/div/ul/li[{i}]/a'))

        # Espera a que el elemento esté presente antes de intentar encontrarlo.

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ctl00_Content_Main_ctl00_Content_Main_MainDivPanel'))
        )

        datos_pagina_actual = driver.find_element(By.CSS_SELECTOR, '#ctl00_Content_Main_ctl00_Content_Main_MainDivPanel').text.split('\n')
        datos_por_pagina[i] = datos_pagina_actual

        driver.back()
        time.sleep(2)
        driver.get('https://rfevb-web.dataproject.com/Statistics.aspx?ID=111&PID=137')

    print('Scraping exitoso')
    return datos_por_pagina
