import requests
from bs4 import BeautifulSoup
import pandas as pd

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

datos.to_parquet('Acciones_lideres.parquet',index=False)

page1 = requests.get('https://bolsar.info/Titulos_Publicos.php')
soup1 = BeautifulSoup(page1.content,'html.parser')
tabla1 = soup1.find('table', id='lideres1')

lista_titulos = []

for fila in tabla1.find_all('tr'):

    datos_filas1 = {}

    celdas1 = fila.find_all('td')

    if celdas1:

        datos_filas1['Especies'] = celdas1[0].get_text()
        datos_filas1['Vto'] = celdas1[1].get_text()
        datos_filas1['Cant. Nominal (Compra)'] = celdas1[2].get_text()
        datos_filas1['Compra'] = celdas1[3].get_text()
        datos_filas1['Venta'] = celdas1[4].get_text()
        datos_filas1['Cant. Nominal (Venta)'] = celdas1[5].get_text()
        datos_filas1['Último'] = celdas1[6].get_text()
        datos_filas1['Variación'] = celdas1[7].get_text()
        datos_filas1['Apertura'] = celdas1[8].get_text()
        datos_filas1['Mín'] = celdas1[9].get_text()
        datos_filas1['Max'] = celdas1[10].get_text()
        datos_filas1['Cierre Anterior'] = celdas1[11].get_text()
        datos_filas1['Volumen'] = celdas1[12].get_text()
        datos_filas1['Monto'] = celdas1[13].get_text()
        datos_filas1['Oper'] = celdas1[14].get_text()
        datos_filas1['Hora'] = celdas1[15].get_text()

        lista_titulos.append(datos_filas1)

datos1 = pd.DataFrame(lista_titulos)

datos1.to_parquet('Titulos.parquet',index=False)

page2 = requests.get('https://bolsar.info/Titulos_Publicos.php')
soup2 = BeautifulSoup(page2.content,'html.parser')
tabla2 = soup2.find('table', id='lideres')

lista_letras = []

for fila in tabla2.find_all('tr'):

    datos_filas2 = {}

    celdas2 = fila.find_all('td')

    if celdas2:

        datos_filas2['Especies'] = celdas2[0].get_text()
        datos_filas2['Vto'] = celdas2[1].get_text()
        datos_filas2['Cant. Nominal (Compra)'] = celdas2[2].get_text()
        datos_filas2['Compra'] = celdas2[3].get_text()
        datos_filas2['Venta'] = celdas2[4].get_text()
        datos_filas2['Cant. Nominal (Venta)'] = celdas2[5].get_text()
        datos_filas2['Último'] = celdas2[6].get_text()
        datos_filas2['Variación'] = celdas2[7].get_text()
        datos_filas2['Apertura'] = celdas2[8].get_text()
        datos_filas2['Mín'] = celdas2[9].get_text()
        datos_filas2['Max'] = celdas2[10].get_text()
        datos_filas2['Cierre Anterior'] = celdas2[11].get_text()
        datos_filas2['Volumen'] = celdas2[12].get_text()
        datos_filas2['Monto'] = celdas2[13].get_text()
        datos_filas2['Oper'] = celdas2[14].get_text()
        datos_filas2['Hora'] = celdas2[15].get_text()

        lista_letras.append(datos_filas2)
    
datos2 = pd.DataFrame(lista_letras)

datos2.to_parquet('Letras.parquet',index=False)

page3 = requests.get('https://bolsar.info/Obligaciones_Negociables.php')
soup3 = BeautifulSoup(page3.content,'html.parser')
tabla3 = soup3.find('table', id='lideres1')

lista_obligaciones = []

for fila in tabla3.find_all('tr'):

    datos_filas3 = {}

    celdas3 = fila.find_all('td')

    if celdas3:

        datos_filas3['Especies'] = celdas3[0].get_text()
        datos_filas3['Vto'] = celdas3[1].get_text()
        datos_filas3['Cant. Nominal (Compra)'] = celdas3[2].get_text()
        datos_filas3['Compra'] = celdas3[3].get_text()
        datos_filas3['Venta'] = celdas3[4].get_text()
        datos_filas3['Cant. Nominal (Venta)'] = celdas3[5].get_text()
        datos_filas3['Último'] = celdas3[6].get_text()
        datos_filas3['Variación'] = celdas3[7].get_text()
        datos_filas3['Apertura'] = celdas3[8].get_text()
        datos_filas3['Mín'] = celdas3[9].get_text()
        datos_filas3['Max'] = celdas3[10].get_text()
        datos_filas3['Cierre Anterior'] = celdas3[11].get_text()
        datos_filas3['Volumen'] = celdas3[12].get_text()
        datos_filas3['Monto'] = celdas3[13].get_text()
        datos_filas3['Oper'] = celdas3[14].get_text()
        datos_filas3['Hora'] = celdas3[15].get_text()

        lista_obligaciones.append(datos_filas3)
    
datos3 = pd.DataFrame(lista_obligaciones)

datos3.to_parquet('Obligaciones.parquet',index=False)