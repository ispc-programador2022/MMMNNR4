from bs4 import BeautifulSoup
import requests
import pandas as pd

url= 'https://www.coingecko.com/es/all-cryptocurrencies'
page= requests.get(url)
soup= BeautifulSoup(page.content,'html.parser')

eq= soup.find_all('span', class_= 'tw-hidden d-lg-block font-bold')
print(eq)

monedas = list()
for i in eq:
    monedas.append(i.text)
print (monedas)