import streamlit as st
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import os
import plotly.express as px
import sys
from src.help_graficos import *

st.set_page_config(page_icon = ':volleyball:', page_title = 'SetyMatchStream')
st.set_option('deprecation.showPyplotGlobalUse', False)

def pagina_inicio():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://integralspor.com/uploads/blog/detail/1618e792d4b1254221.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    

    st.header('Bienvenidos a SetyMatchStream')
    

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
        st.sidebar.write('''🏐 ¡Bienvenidos a SetyMatchStream - tu fuente de análisis profundo y estadísticas del vóleyball! 📊🏐
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

    # Presentación con color de texto personalizado

    presentacion = """<div style="color: #FFFFFF;font-size: 20px;text-shadow: 2px 2px 4px rgba(1,1,1,0.5);">
        Bienvenidos a SetyMatchStream dedicada a las estadísticas de vóley, donde la pasión por el juego se une con el análisis técnico detallado.
        Sumérgete en un mundo de datos precisos y reveladores que iluminan el desempeño de tus equipos y jugadores favoritos.   
        Nos adentramos en los aspectos más técnicos del vóley, desglosando cada partido en números significativos.
        Desde el porcentaje de aciertos en saques hasta la eficacia en los remates, nuestra página ofrece un análisis exhaustivo que va más allá de lo superficial.
        Descubre la magia detrás de cada pase preciso, cada bloqueo exitoso y cómo estas estadísticas se traducen en fortalezas y áreas de mejora para cada equipo.
        Nuestra misión es proporcionarte insights valiosos que te permitan entender a fondo el rendimiento individual y colectivo en la cancha.
        Ya seas un apasionado seguidor del vóley o un analista ávido en busca de datos fundamentales, aquí encontrarás la información adecuada que alimentará tu conocimiento y enriquecerá tu experiencia del juego.
        Conviértete en un experto del vóley mientras exploras nuestras estadísticas detalladas.
        Eleva tu comprensión del juego y únete a una comunidad donde la pasión se combina con la precisión. 
        Entra en el mundo de las estadísticas de vóley, donde cada número cuenta una historia apasionante sobre el emocionante mundo de este deporte.
    </div>"""

    

    image_url = "https://www.purovoley.com/wp-content/uploads/2022/08/Japan-men-2022.png"

    # Diseño de columnas
    columna_texto, columna_imagen = st.columns(2)

    # En la primera columna, coloca el texto con descripción
    columna_texto.markdown(presentacion, unsafe_allow_html=True)

    # Espaciado para centrar verticalmente
    columna_texto.text(" " * 10)

    # En la segunda columna, coloca la imagen con ancho de 1000 píxeles
    columna_imagen.image(image_url, width=1000, use_column_width=True)

    #-----------------------------------------------------------------------------------------------------------

    # SEGUNDA PARTE

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
    columna_izquierda_1, columna_izquierda_2, columna_publicidad = st.columns(3)

    ####### FILTROS ######
    columnas_a_mostrar = ['fecha', 'equipo_local', 'resultado', 'equipo_visitante']

    # FILTRO VACIO JORNADA
    opciones_jornada = [''] + list(jornadas['id_jornada'].unique())

    # FILTRO JORNADA
    valor_filtro = columna_izquierda_1.selectbox("Selecciona una jornada", opciones_jornada, index=0)

    columnas_a_mostrar2 = ['fecha', 'Equipo', 'resultado', 'equipo']

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
        image_url = "https://raw.githubusercontent.com/AlejandroCasna/Proyecto_final/031ed19b42cd79f5bfdf6408194d57fdfe4a4d0e/Imagen/noticia.png"

        # Ajusta el tamaño de la imagen y la hace clickeable
        st.markdown(
            f'<a href="{url}" target="_blank"><img src="{image_url}" width="600"></a>', unsafe_allow_html=True)
        


    clasificacion = pd.read_csv('/ironhack/Proyecto_final/data/2023-2024/Clasificacion.csv')

    # Selecciona solo las columnas que deseas mostrar (por ejemplo, de la columna 2 a la 5)
    clasificacion = clasificacion.iloc[:, 0:6]

    # Establece el estilo de la tabla para cambiar el color de fondo
    st.markdown(
        """
        <style>
        .stTable {
            background-color: #ffffff;  # Puedes cambiar el color de fondo aquí
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Muestra la tabla con el estilo aplicado
    st.dataframe(clasificacion)

    

def estadisticas():
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
    st.markdown("<h1 style='text-align: center;'>Estadísticas de equipo</h1>", unsafe_allow_html=True)


    estadistica = pd.read_csv('../Proyecto_final/posgresSQL/data/estadistica.csv')

    # Filtros
    filtro_equipo = [''] + list(estadistica['Equipo'].unique())
    filtro_temporada = [''] + list(estadistica['temporada'].unique())

    # Barra lateral con filtros
    equipo_seleccionado = st.sidebar.selectbox("Selecciona un Equipo", filtro_equipo)
    temporada_seleccionada = st.sidebar.selectbox("Selecciona una Temporada", filtro_temporada)

    # Filtrar el DataFrame
    if equipo_seleccionado != '' and temporada_seleccionada != '':
        # Aplicar ambos filtros
        estadistica_filtrada = estadistica[
            (estadistica['Equipo'] == equipo_seleccionado) & (estadistica['temporada'] == temporada_seleccionada)
        ]
    elif equipo_seleccionado != '':
        # Aplicar solo el filtro de equipo
        estadistica_filtrada = estadistica[estadistica['Equipo'] == equipo_seleccionado]
    elif temporada_seleccionada != '':
        # Aplicar solo el filtro de temporada
        estadistica_filtrada = estadistica[estadistica['temporada'] == temporada_seleccionada]
    else:
        # No aplicar filtros
        estadistica_filtrada = estadistica

    # Columnas que se mostrarán
    mostrar = ['Equipo', 'Efic_Saque', 'Efic_Recepcion', 'Efic_Ataque', 'Puntos_Set_Bloqueo', 'temporada']

    # Crear un diseño de dos columnas
    col1, col2 = st.columns(2)

    # En la primera columna, mostrar el DataFrame filtrado
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        st.dataframe(estadistica_filtrada[mostrar])

    # En la segunda columna, mostrar el gráfico de araña si se seleccionó un equipo
    with col2:
        st.write('')   
        if equipo_seleccionado:
            araña(equipo_seleccionado)





    st.markdown("<h1 style='text-align: center;'>Estadísticas de jugadores</h1>", unsafe_allow_html=True)

    jugadores = pd.read_csv('../Proyecto_final/posgresSQL/data/jugadores.csv')

    # Initialize
    posicion = None
    equipo = None
    temporada = None

    # Filtros
    filtro_equipo2 = [''] + list(estadistica['Equipo'].unique())
    filtro_temporada2 = [''] + list(jugadores['temporada'].unique())
    filtro_posicion = [''] + list(jugadores['Posicion'].unique())

    st.sidebar.write('---')

    # Barra lateral con filtros
    equipo_seleccionado2 = st.sidebar.selectbox('Selecciona un Equipo', filtro_equipo2, key='equipo_selectbox')
    temporada_seleccionada2 = st.sidebar.selectbox('Selecciona una Temporada', filtro_temporada2, key='temporada_selectbox')
    posicion_seleccionada = st.sidebar.selectbox('Selecciona una Posición', filtro_posicion, key='posicion_selectbox')

    if equipo_seleccionado2 != '':
    # Aplicar solo el filtro de equipo
        equipo = estadistica[estadistica['Equipo'] == equipo_seleccionado2]
    elif temporada_seleccionada2 != '':
        # Aplicar solo el filtro de temporada
        temporada = estadistica[estadistica['temporada'] == temporada_seleccionada2]
    elif temporada_seleccionada2 != '':
        # Aplicar solo el filtro de temporada
        posicion = jugadores[jugadores['Posicion'] == posicion_seleccionada]
    

    
    jugadores = (jugadores[jugadores.Posicion == posicion])
    estadistica = (estadistica[(estadistica['Equipo'] == equipo) & (estadistica['temporada'] == temporada)])


    mostrar = ['Nombre','Posicion','Altura','Ano_de_nacimiento','Alcance_en_ataque','Alcance_en_bloqueo','temporada',]

    merged_df = jugadores.merge(estadistica, on='id_equipo', how='left')

    st.dataframe(merged_df)



























opciones = {
    "Inicio": pagina_inicio,
    "Estadísticas": estadisticas,
    
}
# Sidebar navigation selection
st.sidebar.write("## Navegación")
opcion_seleccionada = st.sidebar.radio("Ir a", list(opciones.keys()))
# Display the selected page
if opcion_seleccionada in opciones:
    opciones[opcion_seleccionada]()














