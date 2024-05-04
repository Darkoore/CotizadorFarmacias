<<<<<<< Updated upstream
=======
from bs4 import BeautifulSoup
import requests

# URL del sitio a scrapear
sitioObjetivo = 'https://www.farmaciasahumada.cl/medicamentos'

# Hacer una solicitud GET al sitio
resultado = requests.get(sitioObjetivo)

# Parsear el contenido HTML de la página
cargarPagina = BeautifulSoup(resultado.content, "lxml")

# Buscar el contenedor principal donde se encuentran los medicamentos
tablasContenidos = cargarPagina.find('div', attrs={'class':"col-sm-12 col-md-9"})
if not tablasContenidos:
    print("No se encontró el contenedor principal de los medicamentos.")

# Listas para almacenar la información recopilada
nombres = []
precios = []
dosises = []
links = []

# Iterar sobre cada elemento que contiene información de un medicamento
if tablasContenidos:
    for contenido in tablasContenidos.find_all('div', attrs={'class':"col-6 col-sm-4 col-lg-3"}):
        nombre = contenido.find('span', attrs={'class':"product-tile-brand"})
        precio = contenido.find('span', attrs={'class':"value d-flex align-items-center"})
        dosis = contenido.find('a', attrs={'class':"link"})
        link = contenido.find('a', attrs={'class':"link"})
        
        # Añadir los resultados a las listas correspondientes
        nombres.append(nombre.text if nombre else "No disponible")
        precios.append(precio.text if precio else "No disponible")
        dosises.append(dosis.text if dosis else "No disponible")
        links.append(link.get("href") if link else "No disponible")

    # Mostrar los resultados
    for i in range(len(nombres)):
        print(f"Nombre: {nombres[i]}, Precio: {precios[i]}, Dosis: {dosises[i]}, Link: {links[i]}")
else:
    print("No se encontraron medicamentos.")


>>>>>>> Stashed changes
