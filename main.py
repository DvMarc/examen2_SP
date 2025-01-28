import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

if "opcion" not in st.session_state:
    st.session_state["opcion"] = "Home"

df = pd.read_excel('Volve production data-1.xlsx', sheet_name='Daily Production Data')

with st.sidebar:
    opcion = option_menu(
        'Seleccione:', 
        ['Home', 'Data', 'Plots'], 
        key='opcion' 
    )

if st.session_state["opcion"] == "Home":
    st.title('Historial de producción del Campo Volve')

    st.write('En esta aplicación se muestra el historial de producción del campo Volve, ubicado en el Mar del Norte, Noruega.')

    st.image('volve.jpg', width=500)
    
elif st.session_state["opcion"] == "Data": 
    st.write("Aquí puedes ver los datos de la produccion diaria.")
    st.write(df)
    st.write("Estos datos son de la producción diaria del campo Volve. Se tienen datos de la producción de petróleo, gas y agua.")
    
elif st.session_state["opcion"] == "Plots":

    st.write("### Gráficas de producción")

    df['DATEPRD'] = pd.to_datetime(df['DATEPRD'])
    df['Year'] = df['DATEPRD'].dt.year


    fig1 = px.line(df, x='DATEPRD', y='BORE_OIL_VOL', color='WELL_BORE_CODE', title='Volumen de petróleo vs Tiempo por Pozo')
    st.plotly_chart(fig1)
    st.write('En esta gráfica se muestra el volumen de petróleo producido por pozo a lo largo del tiempo.')

    fig2 = px.line(df, x='DATEPRD', y='BORE_GAS_VOL', color='WELL_BORE_CODE', title='Volumen de gas vs Tiempo por Pozo')
    st.plotly_chart(fig2)
    st.write('En esta gráfica se muestra el volumen de gas producido por pozo a lo largo del tiempo.')

    fig3 = px.line(df, x='DATEPRD', y=['BORE_OIL_VOL', 'BORE_WAT_VOL'], title='Volumen de petróleo y agua vs Tiempo')
    st.plotly_chart(fig3)
    st.write('En esta gráfica se muestra el volumen de petróleo y agua producido a lo largo del tiempo.')

    total_volumes = df.groupby('WELL_BORE_CODE')[['BORE_OIL_VOL', 'BORE_GAS_VOL', 'BORE_WAT_VOL']].sum().reset_index()
    fig4 = px.bar(total_volumes, x='WELL_BORE_CODE', y=['BORE_OIL_VOL', 'BORE_GAS_VOL', 'BORE_WAT_VOL'], title='Producción total por pozo', barmode='group')
    st.plotly_chart(fig4)
    st.write('En esta gráfica se muestra la producción total de petróleo, gas y agua por pozo.')


