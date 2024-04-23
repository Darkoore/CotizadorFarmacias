<<<<<<< Updated upstream
import requests
from bs4 import BeautifulSoup

@app.route('/scrape')
def scrape():
    # Realizar web scraping
    url = 'https://example.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraer datos
    # ...

    # Renderizar plantilla con los datos obtenidos
    return render_template('scrape_results.html', data=datos_obtenidos)
=======
from bs4 import BeautifulSoup
import requests
import urllib.request

#Resumir sitio a scrapear en una variable
sitioObjetivo = 'https://www.farmaciasahumada.cl/medicamentos'
result = requests.get(sitioObjetivo)
content = result.text

soup = BeautifulSoup(content, 'lxml')
#Esto obtiene la pagina entera
#print(soup.prettify())

#Realiza la busqueda de la clase y la almacena
remedio = soup.find('div', class_='product-tile-brand')

#Busca en la lista almacenada previamente el texto de un archivo span
listaRemedio = remedio.find('span').get_text()

print (listaRemedio)
>>>>>>> Stashed changes
