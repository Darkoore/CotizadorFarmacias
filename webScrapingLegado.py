from bs4 import BeautifulSoup
import requests
import pandas as pd

#Resumir sitio a scrapear en una variable
sitioObjetivo = 'https://www.farmaciasahumada.cl/medicamentos'

resultado = requests.get(sitioObjetivo)
cargarPagina = BeautifulSoup(resultado.content, "lxml")
#Esto obtiene la pagina entera
tablasContenidos = cargarPagina.find('div', attrs={'class':"col-sm-12 col-md-9"})

#https://clarusway.com/your-everyday-superpower-how-to-do-web-scrapping/ desde aca se obtuvo el bloque de codigo de abajo

medicamentoNombres= []
medicamentoPrecios= []
medicamentoDosiss = []
medicamentoLinks  = []


for contenidos in tablasContenidos.find_all('div', attrs={'class':"col-6 col-sm-4 col-lg-3"}):
    medicamentoNombre = contenidos.find('span',attrs={'class':"link"}).get_text()
    medicamentoPrecio = contenidos.find('span',attrs={'class':"value d-flex align-items-center"})
    medicamentoDosis  = contenidos.find('a',attrs={'class':"link"})
    medicamentoLink   = contenidos.find('a',attrs={'class':"link"}).get("href")
    print (medicamentoNombre)
    #print (contenidos)

    #Implementar en medicamentosNombres.csv con Pandas
'''
    medicamentoPrecio = medicamentoPrecio[1:6]

    medicamentoNombres.append(medicamentoNombre)
    medicamentoPrecios.append(medicamentoPrecio)
    medicamentoDosiss.append(medicamentoDosis)
    medicamentoLinks.append(medicamentoLink)

listaMedicamentos = pd.DataFrame({'Medicamento_Nombre:':medicamentoNombres, 'Medicamento_Precio:':medicamentoPrecios, 'Medicamento_Dosis:':medicamentoDosiss, 'Medicamento_Link:':medicamentoLinks})
listaMedicamentos.to_csv("medicamentoNombres.csv")

'''