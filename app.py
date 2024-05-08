import streamlit as st
import pandas as pd

data = pd.read_parquet('Web_scrapp.parquet')

def main():
    st.title('Acciones Líderes')
    st.write(data)

    
if __name__ == "__main__":
    main()
