import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def get_page(url):
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code != 200:
        print(f"Erro: {resp.status_code}")
        return None
    return resp.text
