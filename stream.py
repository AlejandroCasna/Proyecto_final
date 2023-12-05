import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import os
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_icon = ':volleyball:', page_title = 'SetyMatchStream')

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://img.olympics.com/images/image/private/t_s_pog_staticContent_hero_lg_2x/f_auto/primary/tkynwuonkevlorq0r9c7");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

 
# Contenido principal en la barra lateral
st.sidebar.title("Información General")

# Cargar los datos
df = pd.read_csv('..\Proyecto_final\data\Equipos_final.csv')

# Mapear equipos a URLs de imagen
equipos_a_imagenes = {
    'Arenal Emeve': 'https://yt3.googleusercontent.com/ytc/APkrFKYFDxQgjP4QpTyT4l0USR9bKOXH3EjYE54gcVIn8Q=s900-c-k-c0x00ffffff-no-rj',
    'Cisneros Alter': 'https://pbs.twimg.com/profile_images/1715679951054049280/yiauFOvS_400x400.jpg',
    'Manacor':'https://voleimanacor.club/wp-content/uploads/2018/08/logonouok.png',
    'Guaguas': 'https://clubvoleibolguaguas.com/wp-content/uploads/2023/06/Logo-CV-Guaguas-250px.png',
    'CV Melilla':'https://static.flashscore.com/res/image/data/AqSNrktr-IFY3e7TS.png',
    'CV San Roque':'https://clubvoleibolguaguas.com/wp-content/uploads/2023/07/CV-San-Roque-Batan-1269x1280.png',
    'Rio Duero Soria':'https://www.rioduerovoley.com/wp-content/uploads/2021/08/cropped-Rio-Duero-TRANPARENTE-HA.png',
    'CV Teruel' : 'https://i0.wp.com/sextoanillo.com/wp-content/uploads/2022/08/descarga.png?fit=225%2C225&ssl=1',
    'Unicaja Almeria':'https://assets.hypefactors.com/companies/company-logos/cropped/QJKKL8VujtUbZ85DgfAs1voJqcxmAETmsiSyyImF.png',
    'Conqueridor Valencia':'https://plazadeportiva.valenciaplaza.com/public/Image/2022/7/logo-fondogris_NoticiaAmpliada.jpg',
    'CV Villena Petrer':'https://www.comunitatdelesport.com/wp-content/uploads/2021/11/Voley-Petrer.jpg',
    'Barca Voleibol': 'https://volleybox.net/media/upload/teams/1426198410Slzl4.png',
    'Rotogal Boiro':'https://boirovoleibol.com/wp-content/uploads/2021/11/logotipo-VOLEIBOL.fw_.w114px.png',
    'Voley Textil Santanderina':'https://www.rfevb.com/hanImgNot.ashx?src=Logo%20Club-imgEs20221029085114.png&fol=N&Post=Sli',
    'Intasa':'https://i0.wp.com/sextoanillo.com/wp-content/uploads/2021/10/sansadurninho.png?fit=363%2C363&ssl=1',
    'Ibiza Voley':'https://ibi.gsstatic.es/sfAttachPlugin/959745.jpg',
    'Grau':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTA2PH549w2uNdqAaIVg8QzocaiHmL7WCvPayz9z_Pfqz_yJeDgXWe6o-SK_9bytyIitwk&usqp=CAU',
    'Voleibol Almoradi':'https://intranet.rfevb.com/clubes/logos/web/cl00130.png',
    'Vecindario Las Palmas':'https://scontent-mad1-1.xx.fbcdn.net/v/t39.30808-6/300565570_524083349522452_5874749077301041614_n.png?_nc_cat=106&ccb=1-7&_nc_sid=efb6e6&_nc_ohc=9wl7dNNOTC0AX85EBcS&_nc_ht=scontent-mad1-1.xx&oh=00_AfB6Q31hGxtM38yaHxqkUHo8zACQz4hr62POjsrpit65ZQ&oe=6572E458',   
    'Voley Palma': 'https://static.wixstatic.com/media/a88496_ff1acd3ead504b2889816d01bd63b2c3~mv2.jpeg/v1/fit/w_2500,h_1330,al_c/a88496_ff1acd3ead504b2889816d01bd63b2c3~mv2.jpeg'

}

# Barra lateral para seleccionar el equipo
equipo_seleccionado = st.sidebar.selectbox('Seleccione Equipo', ['Seleccione un equipo'] + list(df.Equipo))

# Verificar si se ha seleccionado un equipo
if equipo_seleccionado == 'Seleccione un equipo':
    # Mostrar un mensaje predeterminado
    st.sidebar.write('''🏐 ¡Bienvenidos a SetyMatchStream - tu fuente de análisis profundo y estadísticas del vóley! 📊🏐

Estamos emocionados de sumergirnos en las cifras y datos que definen el rendimiento de los equipos de vóley, tanto en la temporada actual como en las pasadas. Prepárense para un recorrido informativo que iluminará los logros, estrategias y momentos clave que han marcado la historia reciente de este emocionante deporte.

En este espacio, nos sumergiremos en los números, exploraremos tendencias, y desentrañaremos las historias detrás de cada estadística. ¿Cuál equipo tuvo el mejor desempeño en ataques? ¿Quién lidera en bloqueos? ¿Cómo se compara el rendimiento actual con el de temporadas anteriores? Todas estas respuestas y más las descubriremos juntos.

Este no es solo un stream, es una inmersión en la analítica del vóley. Los invito a compartir sus observaciones, hacer preguntas y participar activamente en la conversación estadística. ¡Hagamos de este espacio un encuentro apasionante para los amantes del vóley y los números!

¡Vamos a desmenuzar las estadísticas y a descubrir el verdadero pulso del vóley profesional! 📈🏐 #StatsTalk''')
else:
    # Verificar si el equipo seleccionado tiene una URL de imagen asociada
    if equipo_seleccionado in equipos_a_imagenes:
        url_imagen = equipos_a_imagenes[equipo_seleccionado]
        st.sidebar.markdown(
            f'<img src="{url_imagen}" alt="Imagen de {equipo_seleccionado}" style="border-radius:20%; width:50%;">',
            unsafe_allow_html=True
        )

        # Mostrar información específica de la columna 'informacion' con saltos de línea
        informacion_equipo = df[df['Equipo'] == equipo_seleccionado]['informacion'].iloc[0]
        st.sidebar.markdown(f"\n{informacion_equipo}", unsafe_allow_html=True)

    else:
        st.sidebar.warning(f"No hay URL de imagen asociada para el equipo {equipo_seleccionado}.")



file_path = os.path.abspath('../Proyecto_final/data/2023-2024/Jornadas.csv')
file_path2 = os.path.abspath('../Proyecto_final/jornadas_Streamlit.csv')

st.markdown("""
    <style>
    .title {
        text-align: center;
    }
    </style>
    <h1 class="title">Jornadas Temporada 2023-2024</h1>
    """, unsafe_allow_html=True)

jornadas = pd.read_csv(file_path)
jornadas2 = pd.read_csv(file_path2)
jornadas.reset_index(drop=True, inplace=True)
columna_izquierda_1, columna_izquierda_2 , columna_publicidad= st.columns(3)


####### FILTROS ######
columnas_a_mostrar = ['fecha','equipo_local', 'resultado', 'equipo_visitante']

#FILTRO VACIO JORNADA
opciones_jornada = [''] + list(jornadas['id_jornada'].unique())

# FILTRO JORNADA
valor_filtro = columna_izquierda_1.selectbox("Selecciona una jornada", opciones_jornada, index=0)

columnas_a_mostrar2 = ['fecha','Equipo','resultado', 'equipo'] 

# FILTRO VACIO EQUIPO
opciones_equipo = [''] + list(jornadas2['Equipo'].unique())

# FILTRO EQUIPO
valor_filtro2 = columna_izquierda_2.selectbox("Selecciona un Equipo", opciones_equipo, index=0)

# FILTRO JORNADAS
if valor_filtro:
    jornadas_filtradas = jornadas[jornadas['id_jornada'] == valor_filtro]
    columna_izquierda_1.dataframe(jornadas_filtradas[columnas_a_mostrar], width=800, height=250)

# FILTRO EQUIPOS
if valor_filtro2:
    jornadas_filtradas2 = jornadas2[jornadas2['Equipo'] == valor_filtro2]
    columna_izquierda_2.dataframe(jornadas_filtradas2[columnas_a_mostrar2], width=800, height=250)


with columna_publicidad:
    url = "https://www.rfevb.com/competiciones/superliga-masculina"
    image_path = "../Proyecto_final/noticia.png"
    absolute_path = os.path.abspath(image_path)
    st.markdown(f'[![Noticias de la Jornada]({absolute_path})]({url})', unsafe_allow_html=True) 

    




