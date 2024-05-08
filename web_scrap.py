import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

page = requests.get('https://bolsar.info/lideres.php')
soup = BeautifulSoup(page.content,'html.parser')
tabla = soup.find('table', id='lideres')

lista_lideres = []

for fila in tabla.find_all('tr'):

    datos_filas = {}

    celdas = fila.find_all('td')

    if celdas:

        datos_filas['Especies'] = celdas[0].get_text()
        datos_filas['Vto'] = celdas[1].get_text()
        datos_filas['Cant. Nominal (Compra)'] = celdas[2].get_text()
        datos_filas['Compra'] = celdas[3].get_text()
        datos_filas['Venta'] = celdas[4].get_text()
        datos_filas['Cant. Nominal (Venta)'] = celdas[5].get_text()
        datos_filas['Último'] = celdas[6].get_text()
        datos_filas['Variación'] = celdas[7].get_text()
        datos_filas['Apertura'] = celdas[8].get_text()
        datos_filas['Mín'] = celdas[9].get_text()
        datos_filas['Max'] = celdas[10].get_text()
        datos_filas['Cierre Anterior'] = celdas[11].get_text()
        datos_filas['Volumen'] = celdas[12].get_text()
        datos_filas['Monto'] = celdas[13].get_text()
        datos_filas['Oper'] = celdas[14].get_text()
        datos_filas['Hora'] = celdas[15].get_text()

        lista_lideres.append(datos_filas)
    

datos = pd.DataFrame(lista_lideres)

datos.to_parquet('Web_scrapp.parquet',index=False)