from bs4 import BeautifulSoup

from components.make_request import make_request

def find_element(url, element_tag):
    website = make_request(url)
    if website:
        element = website.find(element_tag)
        if element:
            return element.text.strip()
    
    return None
