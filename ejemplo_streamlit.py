import streamlit as st
import pandas as pd

def main():
    st.title("Cargar archivo en Streamlit")
    
    # Resto del código original

    # Agregar gráfico de barras
    if "acumulada_promedia" not in st.session_state:
        st.session_state.acumulada_promedia = pd.Series([], name="Acumulada Promedio").rename_index(start=1)

    if uploaded_file is not None:
        # Leer el archivo en un DataFrame de Pandas
        df = pd.read_csv(uploaded_file)
        
        # Mostrar el DataFrame
        st.write("Contenido del archivo:")
        st.write(df)

        # Mostrar el gráfico de barras
        st.write("Gráfico de Barras de Acumulada Promedio:")

if __name__ == "__main__":
    main()
