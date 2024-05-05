from bs4 import BeautifulSoup
import requests
import pandas as pd
# URL del sitio a scrapear, cambiar el valor de sz(max 2800) para aumentar el rango del scraping
sitioObjetivo = 'https://www.farmaciasahumada.cl/on/demandware.store/Sites-ahumada-cl-Site/default/Search-UpdateGrid?cgid=medicamentos&start=0&sz=50'

# Hacer una solicitud GET al sitio
resultado = requests.get(sitioObjetivo)

# Parsear el contenido HTML de la página
cargarPagina = BeautifulSoup(resultado.content, "lxml")

# Listas para almacenar la información recopilada
laboratorios = []
precios = []
dosises = []
links = []
data = []
ids = []
id= 0
# Iterar sobre cada elemento que contiene información de un medicamento
if cargarPagina:
    for contenido in cargarPagina.find_all('div', attrs={'class':"col-6 col-sm-4 col-lg-3"}):
        laboratorio = contenido.find('span', attrs={'class':"link"})
        precio = contenido.find('span', attrs={'class':"value d-flex align-items-center"}).text.strip()
        dosis = contenido.find('a', attrs={'class':"link"})
        link = contenido.find('a', attrs={'class':"link"})
        id += 1
        # Añadir los resultados a las listas correspondientes
        ids.append(id)
        laboratorios.append(laboratorio.text if laboratorio else "No disponible")
        precios.append(precio if precio else "No disponible")
        dosises.append(dosis.text if dosis else "No disponible")
        links.append("https://www.farmaciasahumada.cl"+link.get("href") if link else "No disponible")

    # Mostrar los resultados y almacenamiento de datos en un csv
    id = 0
    for i in range(len(laboratorios)):
       
        id += 1
        print("\n---------------------------------------------------------------------",f"\nID: {id}\nNombre: {laboratorios[i]} \nPrecio: {precios[i]} \nDosis: {dosises[i]} \nLink: {links[i]}")
        
        # Creacion de dataframe para generar archivo csv para pandas
        catastro = {
            'ID' : ids,
            'Laboratorio': laboratorios,
            'Precio': precios,
            'Dosis': dosises,
            'Link': links
        }
        dataFrame = pd.DataFrame(catastro)

        # Guardar el DataFrame en un archivo CSV
        dataFrame.to_csv('catalagoAhumada.csv', index=False)
else:
    print("No se encontraron medicamentos.")



