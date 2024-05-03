from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    # Realizar scraping en www.example.com
    url = 'https://www.example.com'
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Obtener el título de la página
        title = soup.title.text

        # Obtener la información de todas las etiquetas meta
        meta_data_list = []
        meta_tags = soup.find_all('meta')
        for tag in meta_tags:
            meta_data_list.append(tag.attrs)

        # Obtener los enlaces de la página
        links = [link['href'] for link in soup.find_all('a')]

        # Renderizar la plantilla index.html y pasar los datos del scraping
        return render_template('index.html', title=title, meta_data_list=meta_data_list, links=links)
    else:
        return "Error al obtener la información del scraping"

if __name__ == '__main__':
    app.run(debug=True)