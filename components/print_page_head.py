from bs4 import BeautifulSoup

from components.make_request import make_request

def print_page_head(url):
    website = make_request(url)
    if website:
        head = website.find('head')
        if head:
            print(head.prettify())