import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


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
                # Verificar si la columna "ACUMULADA PROMEDIO" está presente
        if "ACUMULADA PROMEDIO" in df.columns:
            # Graficar la columna "ACUMULADA PROMEDIO"
            plt.figure(figsize=(10, 6))
            plt.plot(df["ACUMULADA PROMEDIO"])
            plt.title("Gráfico de ACUMULADA PROMEDIO")
            plt.xlabel("Índice")
            plt.ylabel("ACUMULADA PROMEDIO")
            st.pyplot()

if __name__ == "__main__":
    main()
