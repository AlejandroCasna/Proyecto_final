import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('posgresSQL\data\estadistica.csv')
columnas_seleccionadas = ['Equipo', 'Efic_Saque', 'Efic_Recepcion', 'Efic_Ataque', 'Puntos_Set_Bloqueo', 'temporada']
df = df[columnas_seleccionadas]

def araña(equipo):
    # Filter rows where 'Equipo' is equal to the selected team
    df_selected_team = df[df['Equipo'] == equipo]

    # Apply melt to the filtered DataFrame
    df_melt = pd.melt(df_selected_team, id_vars=['Equipo'], var_name='theta', value_name='r')

    # Create the radar chart
    fig = px.line_polar(df_melt, r='r', theta='theta', line_close=True, color='Equipo', line_group='Equipo')

    # Update the traces to fill the area under the line
    fig.update_traces(fill='toself')

    # Update layout for a transparent background
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
        font=dict(size=20, color='black'),  # Larger font size for numbers on axes
    )

    # Update axes titles to be larger and bold
    fig.update_polars(
        angularaxis=dict(
            tickfont=dict(size=25, color='black'),  # Larger font size for axis titles
            linecolor='black',  # Black color for the axis lines
        ),
        radialaxis=dict(
            tickfont=dict(size=20, color='black'),  # Larger font size for numbers on axes
            linecolor='black',  # Black color for the axis lines
        )
    )

    # Display the radar chart in Streamlit
    st.plotly_chart(fig)