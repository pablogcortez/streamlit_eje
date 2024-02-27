import streamlit as st
import pandas as pd

def main():
    st.title("Cargar archivo de Excel en Streamlit")

    # Widget para cargar el archivo de Excel
    uploaded_file = st.file_uploader("Cargar archivo Excel", type=["xlsx"])

    if uploaded_file is not None:
        # Leer el archivo de Excel en un DataFrame de Pandas
        df = pd.read_excel(uploaded_file)
        
        # Mostrar el DataFrame
        st.write("Contenido del archivo Excel:")
        st.write(df)

if __name__ == "__main__":
    main()
