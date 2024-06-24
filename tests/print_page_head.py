from bs4 import BeautifulSoup
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.make_request import make_request

def print_page_head(url):
    soup = make_request(url)
    if soup:
        head = soup.find('head')
        if head:
            print(head.prettify())

def main():
    url = 'https://www.turismo.gov.br/agenda-eventos/views/calendario.php'
    print_page_head(url)

main()