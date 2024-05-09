import streamlit as st
import pandas as pd

data = pd.read_parquet('Web_scrapp.parquet')
data1 = pd.read_parquet('Titulos.parquet')
data2 = pd.read_parquet('Letras.parquet')

def main():
    st.title('Acciones Líderes')
    st.write(data)
    st.title('Títulos')
    st.write(data1)
    st.title('Letras')
    st.write(data2)

    
if __name__ == "__main__":
    main()
