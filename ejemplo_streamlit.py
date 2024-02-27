import streamlit as st
import pandas as pd
import numpy as np

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="Cargar archivo - Mi Aplicación",
        page_icon=":bar_chart:",
        layout="wide"
    )

    # Título de la página
    st.title("Cargar archivo en Streamlit")

    # Widget para cargar el archivo
    uploaded_file = st.file_uploader("Cargar archivo CSV", type=["csv"])

    # Separador
    st.markdown("---")

    if uploaded_file is not None:
        # Leer el archivo en un DataFrame de Pandas
        df = pd.read_csv(uploaded_file)
        
        # Mostrar el DataFrame
        st.write("Contenido del archivo:")
        st.dataframe(df)
        
        # Gráfico de barras
        st.subheader("Gráfico de Barras - ACUMULADA PROMEDIO")
        st.bar_chart(df["ACUMULADA PROMEDIO"])

if __name__ == "__main__":
    main()
