import requests
from bs4 import BeautifulSoup
URL = 'https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07VGRJDFY/ref=sr_1_1_sspa?keywords=switch&qid=1577249133&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQTlIOFlLUFQzTFdSJmVuY3J5cHRlZElkPUEwNzgwMTMxMkNHU0ZQRE5HWlI5MSZlbmNyeXB0ZWRBZElkPUExMDQzMTYyMVRSQk5FREk5SDZLWSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()

    priceconversion = float(price[:-3])
    if priceconversion < 500:
        send_mail()







