import requests
from bs4 import BeautifulSoup
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def make_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        website = BeautifulSoup(response.content, 'html.parser')
        return website
    else:
        print(f"Erro ao requisitar a página: {response.status_code}")
        return None

def main():
    url = 'https://www.turismo.gov.br/agenda-eventos/views/calendario.php'
    website = make_request(url)

    if website:
        print(website.prettify())

main()
