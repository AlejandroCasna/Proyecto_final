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
    

    st.header('Bienvenidos a VoleyStats Pro')

# Enlaces de las imágenes de los logos
    github_logo = "https://icon-library.com/images/github-logo-icon/github-logo-icon-12.jpg"
    linkedin_logo = "https://www.freeiconspng.com/thumbs/linkedin-logo-png/linkedin-logo-0.png"

    # Crea los enlaces con los logos
    github_link = f'<a href="https://github.com/AlejandroCasna"><img src="{github_logo}" width="50"></a>'
    linkedin_link = f'<a href="https://www.linkedin.com/in/alejandrocasna/"><img src="{linkedin_logo}" width="50"></a>'

    # Añade los enlaces a la barra lateral
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

    

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
        st.sidebar.write('''🏐 ¡Bienvenidos a VoleyStats Pro - tu fuente de análisis profundo y estadísticas del vóleyball! 📊🏐 
                         Estamos emocionados de sumergirnos en las cifras y datos que definen el rendimiento de los equipos de vóley, 
                         tanto en la temporada actual como en las pasadas.
                          Prepárense para un recorrido informativo que iluminará los logros,
                          estrategias y momentos clave que han marcado la historia reciente de este emocionante deporte.
                          En este espacio, nos sumergiremos en los números, exploraremos tendencias, y desentrañaremos las historias detrás de cada estadística.
                          ¿Cuál equipo tuvo el mejor desempeño en ataques? ¿Quién lidera en bloqueos? ¿Cómo se compara el rendimiento actual con el de temporadas anteriores?
                          Todas estas respuestas y más las descubriremos juntos. Este no es solo un stream, es una inmersión en la analítica del vóley.
                          ''')

        
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
    Entra en el mundo de las estadísticas de vóley, donde cada número cuenta una historia apasionante sobre el emocionante mundo de este deporte &quot;SetyMatchStream&quot;
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
    
    st.markdown('#### Elije una jornada de juego y conoce los enfrentamientos y resultados de cada equipo')

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
        


    clasificacion = pd.read_csv('/ironhack/Proyecto_final/data/2023-2024/Clasificacion.csv')
    st.markdown("""
        <style>
        .title {
            text-align: center;
        }
        </style>
        <h1 class="title">Tabla de posiciones</h1>
        """, unsafe_allow_html=True)
    
    st.markdown('#### Aqui veras la tabla de resultados en donde figurara semanalmente actualizada las posiciones de los equipos, los partidos jugados, entre ellos los ganados y perdidos y los puntos totales obtenidos hasta el momento.')
 
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

    

def estadisticas():
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://img.olympics.com/images/image/private/t_s_pog_staticContent_hero_lg_2x/f_auto/primary/tkynwuonkevlorq0r9c7");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }}
    .stApp:before {{
        content: '';
        display: block;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        background: rgba(240, 200, 0, 0.1); /* Ajusta la opacidad aquí */
        pointer-events: none; /* Asegúrate de que el pseudo-elemento no capture eventos de clic */
        z-index: -1; /* Coloca el pseudo-elemento detrás del contenido */
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    st.markdown("<h1 style='text-align: center;'>Estadísticas de equipo</h1>", unsafe_allow_html=True)


    estadistica = pd.read_csv('../Proyecto_final/posgresSQL/data/estadistica.csv')

    # Filters
    filtro_equipo = [''] + list(estadistica['Equipo'].unique())
    filtro_temporada = [''] + list(estadistica['temporada'].unique())

    # Sidebar filters
    equipo_seleccionado = st.sidebar.selectbox("Selecciona un Equipo", filtro_equipo)
    temporada_seleccionada = st.sidebar.selectbox("Selecciona una Temporada", filtro_temporada)

    # Filter the DataFrame
    estadistica_filtrada = estadistica.copy()
    if equipo_seleccionado != '':
        estadistica_filtrada = estadistica_filtrada[estadistica_filtrada['Equipo'] == equipo_seleccionado]
    if temporada_seleccionada != '':
        estadistica_filtrada = estadistica_filtrada[estadistica_filtrada['temporada'] == temporada_seleccionada]

    # Graph selector
    opciones_grafico = ['Gráfico de Dona', 'Gráfico de Pastel', 'Gráfico de Barras Apiladas','Gráfico Araña']
    grafico_seleccionado = st.sidebar.selectbox("Selecciona un Gráfico", opciones_grafico)

    # Create a two-column layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<br>", unsafe_allow_html=True)
        mostrar1 = ['Equipo', 'Efic_Saque', 'Efic_Recepcion', 'Efic_Ataque', 'Puntos_Set_Bloqueo','temporada']
        st.dataframe(estadistica_filtrada[mostrar1])

  
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
    
    
    st.markdown("<h1 style='text-align: center;'>Jugadores por equipo</h1>", unsafe_allow_html=True)
    
    jugadores = pd.read_csv('../Proyecto_final/posgresSQL/data/jugadores.csv')
    estadistica = pd.read_csv('../Proyecto_final/posgresSQL/data/estadistica.csv')

    # Inicializar variables
    posicion = None
    equipo = None
    temporada = None

    # Filtros
    filtro_equipo2 = [''] + list(estadistica['Equipo'].unique())
    filtro_temporada2 = [''] + list(jugadores['temporada'].unique())
    filtro_posicion = [''] + list(jugadores['Posicion'].unique())
    filtro_posicion.remove('0')

    st.sidebar.write('---')

    # Barra lateral con filtros
    equipo_seleccionado2 = st.sidebar.selectbox('Selecciona un Equipo', filtro_equipo2, key='equipo_selectbox')
    temporada_seleccionada2 = st.sidebar.selectbox('Selecciona una Temporada', filtro_temporada2, key='temporada_selectbox')
    posicion_seleccionada = st.sidebar.selectbox('Selecciona una Posición', filtro_posicion, key='posicion_selectbox')

    # Aplicar filtros
    if equipo_seleccionado2 != '':
        estadistica = estadistica[estadistica['Equipo'] == equipo_seleccionado2]
    if temporada_seleccionada2 != '':
        jugadores = jugadores[jugadores.temporada == temporada_seleccionada2]
    if posicion_seleccionada != '':
        jugadores = jugadores[jugadores['Posicion'] == posicion_seleccionada]
    

    # Hacer merge de los DataFrames
    mostrar = ['Nombre', 'Posicion', 'Altura', 'Ano_de_nacimiento', 'Alcance_en_ataque', 'Alcance_en_bloqueo', 'temporada']
    merged_df = pd.merge(jugadores, estadistica, on=['id_equipo', 'temporada'], how='inner')[mostrar]



    st.dataframe(merged_df,width=2000,height=300)




#----------------------------------------------------------TERCERA PARTE DE LA PAGINA---------------------------------------------------
    
    
    st.markdown("<h1 style='text-align: center;'>Estadística por jugador</h1>", unsafe_allow_html=True)


    centrales = pd.read_csv('../Proyecto_final/posgresSQL/data/centrales.csv')
    colocadores = pd.read_csv('../Proyecto_final/posgresSQL/data/colocadores.csv')
    liberos = pd.read_csv('../Proyecto_final/posgresSQL/data/liberos.csv')
    opuestos = pd.read_csv('../Proyecto_final/posgresSQL/data/opuestos.csv')
    receptores = pd.read_csv('../Proyecto_final/posgresSQL/data/receptores.csv')
    jugadores = pd.read_csv('../Proyecto_final/posgresSQL/data/jugadores.csv')
    estadistica = pd.read_csv('../Proyecto_final/posgresSQL/data/estadistica.csv')

    if posicion_seleccionada == 'Central':
        jugadores_filtrados = centrales
    elif posicion_seleccionada == 'Colocador':
        jugadores_filtrados = colocadores
    elif posicion_seleccionada == 'Libero':
        jugadores_filtrados = liberos
    elif posicion_seleccionada == 'Opuesto':
        jugadores_filtrados = opuestos
    elif posicion_seleccionada == 'Receptor':
        jugadores_filtrados = receptores
    else:
        jugadores_filtrados = jugadores


    columnas_por_posicion = {
        'Colocador': ['Partidos_jugados', 'Sets_jugados', 'Puntos_negativos', 'Puntos_positivos', 'Acciones_positivas', 'Efic_Ranking', 'temporada'],
        'Central': ['Partidos_jugados', 'Sets_jugados', 'Errores_Saque', 'Porc_error', 'Ataque_Ranking', 'temporada'],
        'Opuesto': ['Partidos_jugados', 'Sets_jugados', 'Porcentaje_error','Ataque_exitoso', 'Porc_error', 'Ataque_Ranking', 'temporada'],
        'Receptor': ['Partidos_jugados', 'Sets_jugados', 'Errores_Saque', 'Porcentaje_error', 'Ataque_exitoso', 'Porc_error', 'Ataque_Ranking', 'temporada'],
        'Libero': ['Partidos_jugados', 'Sets_jugados', 'Puntos_perdidos_recep', 'Puntos_ganados_recep', 'Recep_Ranking', 'temporada']
    }


    columnas_mostrar = columnas_por_posicion.get(posicion_seleccionada, ['Equipo', 'Efic_Saque', 'Efic_Recepcion', 'Efic_Ataque', 'Puntos_Set_Bloqueo','temporada'])

  
    st.dataframe(merged_df,width=2000,height=300)[columnas_mostrar]







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














