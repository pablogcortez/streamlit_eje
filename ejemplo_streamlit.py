import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3

def main():
    st.title("Cargar archivo en Streamlit")

    # Widget para cargar el archivo
    uploaded_file = st.file_uploader("Cargar archivo", type=["csv"])

    if uploaded_file is not None:
        # Leer el archivo en un DataFrame de Pandas
        df = pd.read_csv(uploaded_file)
        
        # Mostrar el DataFrame
        st.write("Contenido del archivo:")
        st.write(df)
        
        # Obtenemos la columna de interés
        acumulada_promedio = df["ACUMULADA PROMEDIO"]
    
        # Crear un gráfico básico de Matplotlib
        fig, ax = plt.subplots()
        ax.plot([1, 2, 3, 4, 5])
    
        # Convertir el gráfico en interactivo con mpld3
        fig_html = mpld3.fig_to_html(fig)
        
        # Mostrar el gráfico interactivo en Streamlit
        st.components.v1.html(fig_html)

if __name__ == "__main__":
    main()
