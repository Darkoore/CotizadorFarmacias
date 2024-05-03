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
        title = soup.title.text
        links = [link['href'] for link in soup.find_all('a')]
        # Renderizar la plantilla index.html y pasar los datos del scraping
        return render_template('index.html', title=title, links=links)
    else:
        return "Error al obtener la información del scraping"

if __name__ == '__main__':
    app.run(debug=True)