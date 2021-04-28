#gets html code from any site 
#obtiene el codigo html de cualquier sitio web

import requests
from bs4 import BeautifulSoup

URL= input('site url: ')
page = requests.get(URL)

soup=BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
