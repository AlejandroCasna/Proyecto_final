import pandas as pd
import plotly.express as px
import streamlit as st

# Lee el archivo CSV y selecciona las columnas deseadas
df = pd.read_csv('..\VoleyStats-Pro\posgresSQL\data\estadistica.csv')
columnas_seleccionadas = ['Equipo', 'Efic_Saque', 'Efic_Recepcion', 'Efic_Ataque', 'Puntos_Set_Bloqueo', 'temporada']
df = df[columnas_seleccionadas]

def araña(equipo):
    # Filtra las filas según el equipo seleccionado en el filtro
    df_selected_team = df[df['Equipo'] == equipo]

    # Aplica el filtro en el DataFrame Melt
    df_melt = pd.melt(df_selected_team, id_vars=['Equipo'], var_name='theta', value_name='r')

    # Crea el gráfico de araña
    fig = px.line_polar(df_melt, r='r', theta='theta', line_close=True, color='Equipo', line_group='Equipo')

    # Actualiza las líneas según cambie el filtro
    fig.update_traces(fill='toself')

    # Actualiza el diseño para un fondo transparente
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  # Fondo transparente
        plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente del gráfico
        font=dict(size=20, color='black'),  # Tamaño de letra más grande para los números en los ejes
    )

    # Actualiza los ejes con títulos más grandes y en negrita
    fig.update_polars(
        angularaxis=dict(
            tickfont=dict(size=25, color='black'),  # Tamaño de letra más grande para los títulos de los ejes
            linecolor='black',  # Color negro para las líneas del eje
        ),
        radialaxis=dict(
            tickfont=dict(size=20, color='black'),  # Tamaño de letra mss grande para los números en los ejes
            linecolor='black',  # Color negro para las lineas del eje
        ),
    )

    # Muestra el gráfico de araña en Streamlit
    st.plotly_chart(fig)


def grafico_barras_apiladas(df):
    # Transforma el DataFrame a un formato largo adecuado para gráficos de barras apiladas
    df_long = df.melt(id_vars=['Equipo', 'temporada'], value_vars=['Efic_Saque', 'Efic_Recepcion', 'Efic_Ataque', 'Puntos_Set_Bloqueo'], var_name='Estadística', value_name='Valor')
    
    # Crea el gráfico de barras apiladas con Plotly Express
    fig = px.bar(df_long, x='temporada', y='Valor', color='Estadística', title="Estadísticas por Temporada")
    
    # Configura el fondo transparente y otros parámetros de estilo
    fig.update_layout(
        paper_bgcolor='rgba(255,255,255,0.2)',  # Fondo transparente del papel
        plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente del gráfico
        font=dict(size=20, color='black'),  # Tamaño de letra más grande para los números en los ejes
        title_font=dict(size=30, color='black'),  # Estilo de la fuente para el título del gráfico
        legend_title_font=dict(size=30, color='white'),  # Estilo de la fuente para el título de la leyenda
        legend_font=dict(size=20, color='black'),  # Estilo de la fuente para los textos de la leyenda
    )
    
    # Muestra el gráfico en Streamlit
    st.plotly_chart(fig)

def grafico_pastel(df):
   
    df_sum = df[['Efic_Saque', 'Efic_Recepcion', 'Efic_Ataque', 'Puntos_Set_Bloqueo']].sum()
    fig = px.pie(names=df_sum.index, values=df_sum.values, title="Distribución de Estadísticas")
    fig.update_layout(
        paper_bgcolor='rgba(255,255,255,0.2)',  # Fondo transparente del papel
        plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente del gráfico
        font=dict(size=20, color='black'),  # Tamaño de letra más grande para los números en los ejes
        title_font=dict(size=30, color='black'),  # Estilo de la fuente para el título del gráfico
        legend_title_font=dict(size=30, color='white'),  # Estilo de la fuente para el título de la leyenda
        legend_font=dict(size=20, color='black'),  # Estilo de la fuente para los textos de la leyenda
    )
    st.plotly_chart(fig)

def grafico_dona(df):
    
    df_sum = df[['Efic_Saque', 'Efic_Recepcion', 'Efic_Ataque', 'Puntos_Set_Bloqueo']].sum()
    fig = px.pie(names=df_sum.index, values=df_sum.values, hole=0.3, title="Distribución de Estadísticas")
    fig.update_layout(
        paper_bgcolor='rgba(255,255,255,0.2)',  # Fondo transparente del papel
        plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente del gráfico
        font=dict(size=20, color='black'),  # Tamaño de letra más grande para los números en los ejes
        title_font=dict(size=30, color='black'),  # Estilo de la fuente para el título del gráfico
        legend_title_font=dict(size=30, color='white'),  # Estilo de la fuente para el título de la leyenda
        legend_font=dict(size=20, color='black'),  # Estilo de la fuente para los textos de la leyenda
    )
    
    st.plotly_chart(fig)

    

    

