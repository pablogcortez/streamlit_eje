import streamlit as st

def calcular_cuadrado(numero):
    return numero ** 2


def main():
    st.title('Calculadora de Cuadrados')

    numero = st.number_input('Ingrese un número', step=1)

    if st.button('Calcular cuadrado'):
        cuadrado = calcular_cuadrado(numero)
        st.success(f'El cuadrado de {numero} es {cuadrado}')


if __name__ == "__main__":
    main()

