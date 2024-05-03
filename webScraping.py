from bs4 import BeautifulSoup
import requests
import urllib.request

#Resumir sitio a scrapear en una variable
sitioObjetivo = 'https://www.farmaciasahumada.cl/medicamentos'

resultado = requests.get(sitioObjetivo)
cargarPagina = BeautifulSoup(resultado.content, "lxml")
#Esto obtiene la pagina entera
tablasContenidos = cargarPagina.find('div', attrs={'class':"col-sm-12 col-md-9"})

#https://clarusway.com/your-everyday-superpower-how-to-do-web-scrapping/ desde aca se obtuvo el bloque de codigo de abajo

medicamentoNombre= []
medicamentoPrecio= []
medicamentoDosis = []
medicamentoLink  = []


for contenidos in tablasContenidos.find_all('div', attrs={'class':"col-6 col-sm-4 col-lg-3"}):
    medicamentoNombre = contenidos.find('span',attrs={'class':"product-tile-brand"})
    medicamentoPrecio = contenidos.find('span',attrs={'class':"value d-flex align-items-center"})
    medicamentoDosis  = contenidos.find('a',attrs={'class':"link"})
    medicamentoLink   = contenidos.find('a',attrs={'class':"link"}).get("href")
    print (medicamentoNombre) 
    '''esta detectando que existen 14 items en la busqueda de linea 21, pero asumo que los .find no estan funcionando
    porque no estan en amarillo'''