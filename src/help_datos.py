import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text, Integer
import re
import warnings

warnings.filterwarnings("ignore")

''' Este archivo incluye estas funciones:

    Mapear nombre de equipos.

    Crear DataFrame: 
    datos: seran los extraidos
    columnas: declaradas por nosotros segun la pagina escrapeada
    parametro:por defecto equipo
    parametro2: jugadores

    '''

def mapear_nombres(equipo):
    mapeo = {
        'Arenal Emevé': 'Arenal Emevé',
        'Arenal Emevé ': 'Arenal Emevé',
        'Barça Voleibol': 'Barça Voleibol',
        'Feníe Energía Mallorca Volei Palma': 'Voley Palma',
        'Voley Palma': 'Voley Palma',
        'Conectabalear CV Manacor': 'Manacor',
        'Manacor': 'Manacor',
        'CV Guaguas': 'Guaguas',
        'Guaguas': 'Guaguas',
        'Léleman VB Valencia': 'Conqueridor Valencia',
        'Valencia': 'Conqueridor Valencia',
        'Melilla Sport Capital': 'CV Melilla',
        'CV Melilla': 'CV Melilla',
        'Club Voleibol Teruel': 'CV Teruel',
        'CV Teruel': 'CV Teruel',
        'Rio Duero Soria': 'Rio Duero Soria',
        'Rotogal Boiro': 'Rotogal Boiro',
        'Rotogal Boiro ': 'Rotogal Boiro',
        'Boiro': 'Rotogal Boiro',
        'Unicaja Costa de Almeria': 'Unicaja Almería',
        'Unicaja Almería': 'Unicaja Almería',
        'Voley Textil Santanderina': 'Voley Textil Santanderina',
        'UD Ibiza Ushuaïa Volley' : 'Ibiza Voley',
        'Ushuaïa Ibiza Voley' : 'Ibiza Voley',
        'Intasa San Sadurniño' : 'Intasa',
        'San Sadurnino' : 'Intasa'
    }

    equipo['Equipo'] = equipo['Equipo'].map(mapeo)

    return equipo



def crear_df(datos,columna ,parametro):
    if parametro == 'equipo':
        filas = [i for i in datos[::2]]
        df = pd.DataFrame(filas, columns=columna)
        print('DataFrame creado!')
        return df

    elif parametro == 'jugadores':
        filas_organizadas = []
        for equipo in datos:
            datos_filas = equipo[7:]
            num_filas = len(datos_filas) // len(columna)
            filas_equipo = [datos_filas[i:i + len(columna)] for i in range(0, len(datos_filas), len(columna))]
            filas_organizadas.extend(filas_equipo)
        jugadores = pd.DataFrame(filas_organizadas, columns=columna)

    elif parametro =='estadistica':
        trozos = [datos[i:i+27] for i in range(2, len(datos), 27)]
        estadistica = pd.DataFrame(trozos, columns=columna)
        convertir = estadistica.columns.difference(['Equipo'])
        columns_to_convert = ['Efic_Ataque', 'Excelente_Ataque', 'Efic_Recepcion', 'Excelente_Recepcion']
        estadistica[columns_to_convert] = estadistica[columns_to_convert].replace('%', '', regex=True)
        estadistica[convertir] = estadistica[convertir].applymap(lambda x: int(x) if str(x).isdigit() else x)
        columns_to_convert = ['Efic_Ataque', 'Excelente_Ataque', 'Efic_Recepcion', 'Excelente_Recepcion', 'Puntos_por_set_Saque', 'Efic_Saque','Puntos_Set_Bloqueo']
        estadistica[columns_to_convert] = estadistica[columns_to_convert].replace({'%': '', ',': '.'}, regex=True).astype(float)
        return estadistica
    
    elif parametro == 'clasificacion':
        rows = [datos[i:i+13] for i in range(0, len(datos), 12)]
        clasificacion = pd.DataFrame(rows, columns=columna)
        return clasificacion
        

    elif parametro == 'estadistica_libero':
        datos = [datos[i:i+13] for i in range(3, len(datos), 13)]
        libero = pd.DataFrame(datos, columns=columna)
        return libero
    
    elif parametro == 'estadistica_receptor':
        datos = [datos[i:i+18] for i in range(3, len(datos), 18)]
        receptor = pd.DataFrame(datos, columns=columna)
        return receptor
    
    elif parametro == 'estadistica_opuesto':
        datos = [datos[i:i+18] for i in range(3, len(datos), 18)]
        opuesto = pd.DataFrame(datos, columns=columna)
        return opuesto
    
    elif parametro == 'estadistica_central':
        datos = [datos[i:i+18] for i in range(3, len(datos), 18)]
        central = pd.DataFrame(datos, columns=columna)
        return central
    
    elif parametro == 'estadistica_colocador':
        datos = [datos[i:i+13] for i in range(3, len(datos), 13)]
        colocador = pd.DataFrame(datos, columns=columna)
        return colocador