import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

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
    st.write("Aquí puedes ver las gráficas.")

