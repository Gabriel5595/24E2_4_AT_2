import requests
from bs4 import BeautifulSoup

def make_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        website = BeautifulSoup(response.content, 'html.parser')
        return website
    else:
        print(f"Erro ao requisitar a página: {response.status_code}")
        return None
