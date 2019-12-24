import requests
from bs4 import BeautfiulSoup
URL = 'https://www.amazon.com/Atelier-Ryza-Darkness-Secret-Hideout-Nintendo/dp/B07TZKVT8W/ref=sr_1_2?crid=K8CWAUCW046V&keywords=atelier%2Bryza%2Bswitch&qid=1577158970&sprefix=atelier%2Bryza%2B%2Caps%2C228&sr=8-2&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

page = requests.get(URL, headers = headers)

