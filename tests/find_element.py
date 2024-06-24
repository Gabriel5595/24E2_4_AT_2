from bs4 import BeautifulSoup
from urllib.error import HTTPError
import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.make_request import make_request

def find_element(url, element_tag):
    try:
        website = make_request(url)
        if website:
            element = website.find(element_tag)
            if element:
                return element.text.strip()
            else:
                print(f"Elemento '{element_tag}' não encontrado na página.")
                return False
    except HTTPError as e:
        print(f"Erro HTTP ao acessar a página: {e}")
        return False
    except Exception as e:
        print(f"Erro ao buscar elemento '{element_tag}': {e}")
        return False

def main():
    url = 'https://www.turismo.gov.br/agenda-eventos/views/calendario.php'
    element_tag = 'title'
    element_content = find_element(url, element_tag)
    if element_content:
        print(f"Conteúdo do elemento '{element_tag}': {element_content}")
    else:
        print(f"Elemento '{element_tag}' não encontrado.")

main()
