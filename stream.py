import streamlit as st
import pandas as pd
from PIL import Image
import webbrowser
import base64
import io
import os
import sys
from src.help_graficos import *



st.set_page_config(page_icon = ':volleyball:', page_title = 'VoleyStats Pro')
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
    

    header_style = """
    <style>
    .stApp {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .header-styles {
        font-size: 40px;
        font-weight: bold;
        color: #FF4B4B;  /* Cambia el color según tus preferencias */
        text-align: center;
        padding: 10px;
        background-color: #F0F2F6;  /* Fondo del encabezado */
        border-radius: 10px;  /* Bordes redondeados */
        margin: 25px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);  /* Sombra para dar efecto de elevación */
    }
    </style>
    """

    # Inyecta el CSS en la aplicación de Streamlit
    st.markdown(header_style, unsafe_allow_html=True)

    # Usa una clase personalizada para el encabezado
    st.markdown('<div class="header-styles">Bienvenidos a VoleyStats Pro</div>', unsafe_allow_html=True)

    col1, col2 = st.sidebar.columns(2)
    with col1:
        # logo para cuenta personal
        github_logo = "https://icon-library.com/images/github-logo-icon/github-logo-icon-12.jpg"

        # los crea dentro de la imagen 
        github_link = f'<a href="https://github.com/AlejandroCasna"><img src="{github_logo}" width="50"></a>'

        # Añade los enlaces a la barra lateral
        st.sidebar.markdown(github_link, unsafe_allow_html=True)
    with col2:
        linkedin_logo = "https://www.freeiconspng.com/thumbs/linkedin-logo-png/linkedin-logo-0.png"
        linkedin_link = f'<a href="https://www.linkedin.com/in/alejandrocasna/"><img src="{linkedin_logo}" width="50"></a>'
        st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)


    

  
    df = pd.read_csv('../VoleyStats-Pro/data/Equipos_final.csv')

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

    # Verificar si el equipo seleccionado tien imagen asociada
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
        st.sidebar.warning(f"Seleccione un equipo para más información {equipo_seleccionado}.")

    # Presentación con color de texto personalizado

    presentacion = """<div style='color: #FFFFFF;font-size: 20px;text-shadow: 2px 2px 4px rgba(1,1,1,0.5); text-align: justify;'>
    Bienvenidos a VoleyStats Pro, dedicada a las estadísticas de vóley, donde la pasión por el juego se une con el análisis técnico detallado.
    Sumérgete en un mundo de datos precisos y reveladores que iluminan el desempeño de tus equipos y jugadores favoritos.
    Nos adentramos en los aspectos más técnicos del vóley, desglosando cada partido en números significativos.
    Desde el porcentaje de aciertos en saques hasta la eficacia en los remates, nuestra página ofrece un análisis exhaustivo que va más allá de lo superficial.
    Descubre la magia detrás de cada pase preciso, cada bloqueo exitoso y cómo estas estadísticas se traducen en fortalezas y áreas de mejora para cada equipo. 
    Nuestra misión es proporcionarte insights valiosos que te permitan entender a fondo el rendimiento individual y colectivo en el campo de cada equipo. 
    Ya seas un apasionado seguidor del vóley o un analista ávido en busca de datos fundamentales, 
    aquí encontrarás la información adecuada que alimentará tu conocimiento y enriquecerá tu experiencia del juego.
    Eleva tu comprensión del juego y únete a una comunidad donde la pasión se combina con la precisión. 
    Entra en el mundo de las estadísticas de vóley, donde cada número cuenta una historia apasionante sobre el emocionante mundo de este deporte.
</div>"""

    

    image_url = "https://www.purovoley.com/wp-content/uploads/2022/08/Japan-men-2022.png"

    # diseño de la primera caja. lo divido en 2 sectores
    columna_texto, columna_imagen = st.columns(2)

    # primer columna texto
    columna_texto.markdown(presentacion, unsafe_allow_html=True)

    # Espacias
    columna_texto.text(" " * 10)

    # segunda columna imagen
    columna_imagen.image(image_url, width=1000, use_column_width=True)

                    #-----------------------------------------------------------------------------------------------------------

    # SEGUNDA PARTE

    file_path = os.path.abspath('../VoleyStats-Pro/data/2023-2024/Jornadas.csv')
    file_path2 = os.path.abspath('../VoleyStats-Pro/jornadas_Streamlit.csv')

    header_style = """
   <style>
    .stApp {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .header-styles {
    font-size: 40px;
    font-weight: bold;
    color: #000000;  /* Cambiado a negro */
    text-align: center;
    padding: 10px;
    background-color: #F0F2F6;  /* Fondo del encabezado */
    border-radius: 10px;  /* Bordes redondeados */
    margin: 25px;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);  /* Sombra para dar efecto de elevación */
}
</style>
    """

    # Inyecta el CSS en la aplicación de Streamlit
    st.markdown(header_style, unsafe_allow_html=True)

    # Usa una clase personalizada para el encabezado
    st.markdown('<div class="header-styles">Jornadas temporada 2023-2024</div>', unsafe_allow_html=True)

    jornadas = pd.read_csv(file_path)
    jornadas2 = pd.read_csv(file_path2)
    jornadas.reset_index(drop=True, inplace=True)
    columna_izquierda_1, columna_izquierda_2, columna_publicidad = st.columns(3)

    ####### FILTROS ######
    columnas_a_mostrar = ['fecha', 'equipo_local', 'resultado', 'equipo_visitante']

    # FILTRO VACIO JORNADA
    opciones_jornada = ['Selecciona un número de jornada.'] + list(jornadas['id_jornada'].unique())

    # FILTRO JORNADA
    valor_filtro = columna_izquierda_1.selectbox("Selecciona una jornada", opciones_jornada, index=0)

    columnas_a_mostrar2 = ['fecha', 'Equipo', 'resultado', 'equipo']

    # FILTRO VACIO EQUIPO
    opciones_equipo = ['Selecciona un Equipo.'] + list(jornadas2['Equipo'].unique())
    

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
        


    clasificacion = pd.read_csv('../VoleyStats-Pro/data/2023-2024/Clasificacion.csv')
    
    header_style = """
    <style>
    .stApp {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .header-styles {
        font-size: 40px;
        font-weight: bold;
        color: #FF4B4B;  /* Cambia el color según tus preferencias */
        text-align: center;
        padding: 10px;
        background-color: #F0F2F6;  /* Fondo del encabezado */
        border-radius: 10px;  /* Bordes redondeados */
        margin: 25px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);  /* Sombra para dar efecto de elevación */
    }
    </style>
    """

    # Inyecta el CSS en la aplicación de Streamlit
    st.markdown(header_style, unsafe_allow_html=True)

    # Usa una clase personalizada para el encabezado
    st.markdown('<div class="header-styles">Tabla de posiciones</div>', unsafe_allow_html=True)
 
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
    
    st.dataframe(clasificacion,width=2000,height=400)

def estadisticas_equipo():
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
    

    header_style = """
    <style>
    .stApp {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .header-styles {
        font-size: 40px;
        font-weight: bold;
        color: #FF4B4B;  /* Cambia el color según tus preferencias */
        text-align: center;
        padding: 10px;
        background-color: #F0F2F6;  /* Fondo del encabezado */
        border-radius: 10px;  /* Bordes redondeados */
        margin: 25px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);  /* Sombra para dar efecto de elevación */
    }
    </style>
    """

    # Inyecta el CSS en la aplicación de Streamlit
    st.markdown(header_style, unsafe_allow_html=True)

    # Usa una clase personalizada para el encabezado
    st.markdown('<div class="header-styles">Estadísticas por equipo</div>', unsafe_allow_html=True)


    estadistica = pd.read_csv('../VoleyStats-Pro/posgresSQL/data/estadistica.csv')

    # filtros
    filtro_equipo = [''] + list(estadistica['Equipo'].unique())
    filtro_temporada = [''] + list(estadistica['temporada'].unique())


    st.sidebar.write('---')
    st.sidebar.title('Estadísticas de equipo.')
    # filtros lateral
    equipo_seleccionado = st.sidebar.selectbox("Selecciona un Equipo", filtro_equipo)
    temporada_seleccionada = st.sidebar.selectbox("Selecciona una Temporada", filtro_temporada)

    # filtros del dataframe
    estadistica_filtrada = estadistica.copy()
    if equipo_seleccionado != '':
        estadistica_filtrada = estadistica_filtrada[estadistica_filtrada['Equipo'] == equipo_seleccionado]
    if temporada_seleccionada != '':
        estadistica_filtrada = estadistica_filtrada[estadistica_filtrada['temporada'] == temporada_seleccionada]

    # selector de grafico
    opciones_grafico = ['Gráfico de Dona', 'Gráfico de Pastel', 'Gráfico de Barras Apiladas','Gráfico Araña']
    grafico_seleccionado = st.sidebar.selectbox("Selecciona un Gráfico", opciones_grafico)

    # dividimos ese sector en 2
    col1, col2 = st.columns(2)
    
    #el primero dataframe
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        mostrar1 = ['Equipo', 'Efic_Saque', 'Efic_Recepcion', 'Efic_Ataque', 'Puntos_Set_Bloqueo','temporada']
        st.dataframe(estadistica_filtrada[mostrar1])

    # el segundo los graficos creados en help_graficos
    with col2:
        if grafico_seleccionado == 'Gráfico de Dona':
            grafico_dona(estadistica_filtrada)
        elif grafico_seleccionado == 'Gráfico de Pastel':
            grafico_pastel(estadistica_filtrada)
        elif grafico_seleccionado == 'Gráfico de Barras Apiladas':
            grafico_barras_apiladas(estadistica_filtrada)
        elif grafico_seleccionado == 'Gráfico Araña':
            araña(equipo_seleccionado)

    
   
    



                                #----------------------------------------------------------SEGUNDA PARTE DE LA PAGINA---------------------------------------------------
    
def jugadores_equipo():
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
    

    header_style = """
    <style>
    .stApp {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .header-styles {
        font-size: 40px;
        font-weight: bold;
        color: #FF4B4B;  /* Cambia el color según tus preferencias */
        text-align: center;
        padding: 10px;
        background-color: #F0F2F6;  /* Fondo del encabezado */
        border-radius: 10px;  /* Bordes redondeados */
        margin: 25px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);  /* Sombra para dar efecto de elevación */
    }
    </style>
    """

    # Inyecta el CSS en la aplicación de Streamlit
    st.markdown(header_style, unsafe_allow_html=True)

    # Usa una clase personalizada para el encabezado
    st.markdown('<div class="header-styles">Jugadores por equipo</div>', unsafe_allow_html=True)
    
    
    jugadores = pd.read_csv('../VoleyStats-Pro/posgresSQL/data/jugadores.csv')
    estadistica = pd.read_csv('../VoleyStats-Pro/posgresSQL/data/estadistica.csv')

    # en base a pruebas fue necesario iniciarlas vacias
    posicion = None
    equipo = None
    temporada = None

    # filtros
    filtro_equipo2 = [''] + list(estadistica['Equipo'].unique())
    filtro_temporada2 = [''] + list(jugadores['temporada'].unique())
    filtro_posicion = [''] + list(jugadores['Posicion'].unique())
    filtro_posicion.remove('0')

    st.sidebar.write('---')
    st.sidebar.title('Jugadores por equipo.')

    # filtros laterales
    equipo_seleccionado2 = st.sidebar.selectbox('Selecciona un Equipo', filtro_equipo2, key='equipo_selectbox')
    temporada_seleccionada2 = st.sidebar.selectbox('Selecciona una Temporada', filtro_temporada2, key='temporada_selectbox')
    posicion_seleccionada = st.sidebar.selectbox('Selecciona una Posición', filtro_posicion, key='posicion_selectbox')

    # filtros
    if equipo_seleccionado2 != '':
        estadistica = estadistica[estadistica['Equipo'] == equipo_seleccionado2]
    if temporada_seleccionada2 != '':
        jugadores = jugadores[jugadores.temporada == temporada_seleccionada2]
    if posicion_seleccionada != '':
        jugadores = jugadores[jugadores['Posicion'] == posicion_seleccionada]
    

    # merge para coger toda la informacion necesaria
    mostrar = ['Nombre', 'Posicion', 'Altura', 'Ano_de_nacimiento', 'Alcance_en_ataque', 'Alcance_en_bloqueo', 'temporada']
    merged_df = pd.merge(jugadores, estadistica, on=['id_equipo', 'temporada'], how='inner')[mostrar]



    st.dataframe(merged_df,width=2000,height=600)




           #----------------------------------------------------------TERCERA PARTE DE LA PAGINA---------------------------------------------------
     
def estadisticas_jugadores():
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
    

    header_style = """
    <style>
    .stApp {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .header-styles {
        font-size: 40px;
        font-weight: bold;
        color: #FF4B4B;  /* Cambia el color según tus preferencias */
        text-align: center;
        padding: 10px;
        background-color: #F0F2F6;  /* Fondo del encabezado */
        border-radius: 10px;  /* Bordes redondeados */
        margin: 25px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);  /* Sombra para dar efecto de elevación */
    }
    </style>
    """

    # Inyecta el CSS en la aplicación de Streamlit
    st.markdown(header_style, unsafe_allow_html=True)

    # Usa una clase personalizada para el encabezado
    st.markdown('<div class="header-styles">Estadística por jugador</div>', unsafe_allow_html=True)




    df_posicion_filtrado= None
    df_equipo = pd.read_csv('../VoleyStats-Pro/posgresSQL/data/Equipos.csv')
    df_jugadores = pd.read_csv('../VoleyStats-Pro/posgresSQL/data/jugadores.csv')
    df_opuesto = pd.read_csv('../VoleyStats-Pro/posgresSQL/data/opuestos.csv')
    df_central = pd.read_csv('../VoleyStats-Pro/posgresSQL/data/centrales.csv')
    df_colocador = pd.read_csv('../VoleyStats-Pro/posgresSQL/data/colocadores.csv')
    df_libero = pd.read_csv('../VoleyStats-Pro/posgresSQL/data/liberos.csv')
    df_receptor = pd.read_csv('../VoleyStats-Pro/posgresSQL/data/receptores.csv')


    st.sidebar.write('---')
    st.sidebar.title('Estadísticas por jugador.')
    # Crear los filtros en el sidebar
    seleccion1 = st.sidebar.selectbox('Selecciona un equipo', df_equipo['Equipo'].unique())
    seleccion2 = st.sidebar.selectbox('Selecciona una temporada', df_jugadores['temporada'].unique())
    seleccion3 = st.sidebar.selectbox('Selecciona una posición', df_jugadores['Posicion'].unique())
    

    posicion_seleccionada = seleccion3
    

    df_jugadores_filtrado = df_jugadores[(df_jugadores['id_equipo'] == df_equipo[df_equipo['Equipo'] == seleccion1]['id_equipo'].values[0]) & 
                                        (df_jugadores['temporada'] == seleccion2) & 
                                        (df_jugadores['Posicion'] == posicion_seleccionada)]
    
    columnas_opuesto = ['Nombre','Partidos_jugados','Sets_jugados','Bloqueo_exitoso','Bloqueo_fallido','Total_bloqueos','Errores_Saque','Porcentaje_error','Total_saques','Errores_ataque','Porc_error','Total_ataques','Ataque_Ranking','temporada']
    columnas_central = ['Nombre','Partidos_jugados','Sets_jugados','Bloqueo_exitoso','Bloqueo_fallido','Total_bloqueos','Errores_Saque','Porcentaje_error','Total_saques','Ataque_exitoso','Errores_ataque','Porc_error','Total_ataques','Ataque_Ranking','temporada']
    columnas_colocador = ['Nombre','Partidos_jugados','Sets_jugados','Acciones_exitosas','Errores_colocador','Puntos_negativos','Puntos_positivos','Acciones_positivas','Total_acumulado','Efic_Ranking','temporada']
    columnas_libero = ['Nombre','Partidos_jugados','Sets_jugados','Recepciones_exitosas','Recepciones_fallidas','Recep_Ranking','temporada']
    columnas_receptor = ['Nombre','Partidos_jugados','Sets_jugados','Bloqueo_exitoso','Bloqueo_fallido','Total_bloqueos','Errores_Saque','Porcentaje_error','Total_saques','Ataque_exitoso','Errores_ataque','Porc_error','Total_ataques','Ataque_Ranking','temporada']

    # Filtrar el dataframe correspondiente a la posición seleccionada y seleccionar las columnas deseadas
    if posicion_seleccionada.lower() == 'opuesto':
        df_posicion_filtrado = df_opuesto[df_opuesto['id_jugador'].isin(df_jugadores_filtrado['id_jugador'])][columnas_opuesto]
    elif posicion_seleccionada.lower() == 'Middle-blocker':
        df_posicion_filtrado = df_central[df_central['id_jugador'].isin(df_jugadores_filtrado['id_jugador'])][columnas_central]
    elif posicion_seleccionada.lower() == 'colocador':
        df_posicion_filtrado = df_colocador[df_colocador['id_jugador'].isin(df_jugadores_filtrado['id_jugador'])][columnas_colocador]
    elif posicion_seleccionada.lower() == 'libero':
        df_posicion_filtrado = df_libero[df_libero['id_jugador'].isin(df_jugadores_filtrado['id_jugador'])][columnas_libero]
    elif posicion_seleccionada.lower() == 'receptor':
        df_posicion_filtrado = df_receptor[df_receptor['id_jugador'].isin(df_jugadores_filtrado['id_jugador'])][columnas_receptor]
    else:
        st.error("Posición no reconocida")
        

    # Mostrar la información de los jugadores en el dataframe filtrado
    if df_posicion_filtrado is not None:
        st.dataframe(df_posicion_filtrado,width=2000,height=300)
    else:
        st.write("No hay datos para mostrar.")






opciones = {
    "Inicio": pagina_inicio,
    "Estadísticas por equipo": estadisticas_equipo,
    "Jugadores por equipo": jugadores_equipo,
    "Estadísticas de jugadores": estadisticas_jugadores
    }

# Sidebar navigation selection
st.sidebar.write("## Navegación")
opcion_seleccionada = st.sidebar.radio("",list(opciones.keys()))
# Display the selected page
if opcion_seleccionada in opciones:
    opciones[opcion_seleccionada]()














