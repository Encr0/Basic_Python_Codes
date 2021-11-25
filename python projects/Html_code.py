#gets html code from any site/ ur stupid if u think u going to get database and that stuff :u
#obtiene el codigo html de cualquier sitio web
#maded by Pablo :^

import requests
from bs4 import BeautifulSoup

URL= input('site url: ')
page = requests.get(URL)

soup=BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
