<<<<<<< Updated upstream
#TESTING.........................
=======
import requests
from bs4 import BeautifulSoup
from jinja2 import Template

# URL de la página web a la que queremos hacer scraping
url = 'https://www.example.com'

# Realizar una solicitud HTTP GET a la página web
response = requests.get(url)
print(response.status_code)
# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener el contenido HTML de la página web
    html_content = response.text

    # Analizar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # En este ejemplo, vamos a extraer el título de la página
    title = soup.title.text

    # También podríamos extraer otros elementos, como enlaces <a>, imágenes <img>, etc.
    # Por ejemplo, para extraer todos los enlaces de la página:
    links = [link['href'] for link in soup.find_all('a')]

    # Cargar la plantilla HTML
    with open('templates/index.html', 'r') as file:
        template_content = file.read()

    # Compilar la plantilla
    template = Template(template_content)

    # Renderizar la plantilla con la información obtenida del scraping
    rendered_html = template.render(title=title, links=links)

    # Guardar el HTML renderizado en un archivo
    with open('output.html', 'w') as file:
        file.write(rendered_html)

    print("Documento HTML generado correctamente.")

else:
    print("Error al realizar la solicitud HTTP:", response.status_code)
>>>>>>> Stashed changes
