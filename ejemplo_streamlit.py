import streamlit as st
import pandas as pd

def main():
    st.title("Cargar archivo en Streamlit")

    if uploaded_file is not None:
        # Leer el archivo en un DataFrame de Pandas
        df = pd.read_csv(uploaded_file)
        
        # Mostrar el DataFrame
        st.write("Contenido del archivo:")
        st.write(df)


if __name__ == "__main__":
    main()
