import pandas as pd
import plotly.express as px
import streamlit as st


df = pd.read_csv('..\VoleyStats-Pro\postgresSQL\data\estadistica.csv')
columnas_seleccionadas = ['Equipo', 'Efic_Saque', 'Efic_Recepcion', 'Efic_Ataque', 'Puntos_Set_Bloqueo', 'temporada']
df = df[columnas_seleccionadas]

def araña(equipo):
    df_selected_team = df[df['Equipo'] == equipo]

    df_melt = pd.melt(df_selected_team, id_vars=['Equipo'], var_name='theta', value_name='r')

    # Crea el gráfico de araña
    fig = px.line_polar(df_melt, r='r', theta='theta', line_close=True, color='Equipo', line_group='Equipo')

    # Actualiza las líneas según cambie el filtro
    fig.update_traces(fill='toself')

    fig.update_layout(
        paper_bgcolor='rgba(255,255,255,0.6)',  # Slightly transparent background for better readability
        plot_bgcolor='rgba(255,255,255,0.9)',  # Slightly transparent chart background
        font=dict(size=20, color='black'),  # Font size and color for better readability
        legend=dict(
            x=1,  # Move the legend to the right
            y=1,  # Move the legend to the top
            bgcolor='rgba(255,255,255,0.8)',  # Slightly transparent background for the legend
            bordercolor='Black',  # Legend border color
            borderwidth=1,  # Legend border width
            font=dict(
                size=14,  # Font size for the legend
                color='black'  # Font color for the legend
            )
        ),
        title=dict(
            text='Estadísticas de Equipo',  # Descriptive title
            x=0.5,  # Center the title
            y=0.95,  # Adjust the Y position of the title
            xanchor='center',  # Ensure the title is centered
            yanchor='top',  # Ensure the title is at the top
            font=dict(size=24, color='black')  # Title font size and color
        )
    )

    # Update the polar axes with larger and bold titles
    fig.update_polars(
        angularaxis=dict(
            tickfont=dict(size=20, color='black'),  # Larger font size for axis titles
            linecolor='black',  # Black color for axis lines
        ),
        radialaxis=dict(
            tickfont=dict(size=20, color='black'),  # Larger font size for axis numbers
            linecolor='black',  # Black color for axis lines
        ),
    )

    # Display the radar chart in Streamlit
    st.plotly_chart(fig)


def grafico_barras_apiladas(df):
    rounded_border_style = """
    <style>
    div.stPlotlyChart > div {
        border-radius: 15px;  /* Ajusta esto para cambiar el radio del borde */
        box-shadow: 0px 0px 10px rgba(0,0,0,0.15);  /* Sombra para dar un efecto elevado */
        overflow: hidden;  /* Asegura que el borde redondeado se aplique */
        background-color: rgba(255,255,255,0.2);  /* Fondo transparente con bordes redondeados */
    }
    </style>
    """

    # Inyecta el CSS en la aplicación de Streamlit
    st.markdown(rounded_border_style, unsafe_allow_html=True)

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
    rounded_border_style = """
    <style>
    div.stPlotlyChart > div {
        border-radius: 15px;  /* Ajusta esto para cambiar el radio del borde */
        box-shadow: 0px 0px 10px rgba(0,0,0,0.15);  /* Sombra para dar un efecto elevado */
        overflow: hidden;  /* Asegura que el borde redondeado se aplique */
        background-color: rgba(255,255,255,0.2);  /* Fondo transparente con bordes redondeados */
    }
    </style>
    """

    # Inyecta el CSS en la aplicación de Streamlit
    st.markdown(rounded_border_style, unsafe_allow_html=True)

    # Crea el gráfico de pastel
    df_sum = df[['Efic_Saque', 'Efic_Recepcion', 'Efic_Ataque', 'Puntos_Set_Bloqueo']].sum()
    fig = px.pie(names=df_sum.index, values=df_sum.values, title="Distribución de Estadísticas")
    fig.update_layout(
        paper_bgcolor='rgba(255,255,255,0.2)',  # Fondo transparente del papel
        plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente del gráfico
        font=dict(size=20, color='black'),  # Tamaño de letra más grande para los números en los ejes
        title_font=dict(size=30, color='black'),  # Estilo de la fuente para el título del gráfico
        legend_title_font=dict(size=30, color='white'),  # Estilo de la fuente para el título de la leyenda
        legend_font=dict(size=20, color='black'),  # Estilo de la fuente para los textos de la leyenda
        showlegend=True,  # Asegúrate de que la leyenda se muestre
        legend=dict(
            bgcolor='rgba(255,255,255,0.6)',  # Fondo ligeramente transparente para la leyenda
            bordercolor='rgba(0,0,0,0.5)',  # Color del borde de la leyenda
            borderwidth=2,  # Ancho del borde de la leyenda
            x=0.9,  # Posición horizontal de la leyenda
            y=1.2,  # Posición vertical de la leyenda
        )
    )

    # Añade bordes redondeados y sombra al contenedor del gráfico
    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))  # Borde negro para las porciones del pastel

    # Muestra el gráfico de pastel en Streamlit
    st.plotly_chart(fig)

def grafico_dona(df):
    rounded_border_style = """
<style>
div.stPlotlyChart > div {
    border-radius: 15px;  /* Ajusta esto para cambiar el radio del borde */
    box-shadow: 0px 0px 10px rgba(0,0,0,0.15);  /* Sombra para dar un efecto elevado */
    overflow: hidden;  /* Asegura que el borde redondeado se aplique */
}
</style>
"""

# Inyecta el CSS en la aplicación de Streamlit
    st.markdown(rounded_border_style, unsafe_allow_html=True)


    df_sum = df[['Efic_Saque', 'Efic_Recepcion', 'Efic_Ataque', 'Puntos_Set_Bloqueo']].sum()
    fig = px.pie(names=df_sum.index, values=df_sum.values, hole=0.3, title='Gráfico')

    # Actualiza el diseño del gráfico para incluir bordes redondeados y sombra
    fig.update_layout(
        paper_bgcolor='rgba(255,255,255,0.2)',  # Fondo transparente del papel
        plot_bgcolor='rgba(0,0,0,0)',  # Fondo transparente del gráfico
        font=dict(size=20, color='black'),  # Tamaño de letra más grande para los números en los ejes
        title_font=dict(size=30, color='black'),  # Estilo de la fuente para el título del gráfico
        legend_title_font=dict(size=30, color='white'),  # Estilo de la fuente para el título de la leyenda
        legend_font=dict(size=20, color='black'),  # Estilo de la fuente para los textos de la leyenda
        showlegend=True,  # Asegúrate de que la leyenda se muestre
        legend=dict(
            bgcolor='rgba(255,255,255,0.6)',  # Fondo ligeramente transparente para la leyenda
            bordercolor='rgba(0,0,0,0.5)',  # Color del borde de la leyenda
            borderwidth=2,  # Ancho del borde de la leyenda
            x=0.9,  # Posición horizontal de la leyenda
            y=1.2,  # Posición vertical de la leyenda
        )
    )

    # Añade bordes redondeados y sombra al contenedor del gráfico
    fig.update_traces(marker=dict(line=dict(color='#000000', width=2)))  # Borde negro para las porciones del pastel
    fig.add_layout_image(
        dict(

            xref="paper", yref="paper",
            x=0.5, y=0.5,
            sizex=0.8, sizey=0.8,
            xanchor="center", yanchor="middle",
            layer="below"
        )
    )

    # Muestra el gráfico de pastel en Streamlit
    st.plotly_chart(fig)

    

    

