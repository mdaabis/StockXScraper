import requests
from bs4 import BeautifulSoup
from decouple import config
import json
import pandas as pd
from stockxsdk import Stockx

stockx = Stockx()
email = config('EMAIL')
password = config('PASSWORD')
url = 'https://stockx.com/api/products/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}


def highest_bid():
    page = url + '5e6a1e57-1c7d-435a-82bd-5666a13560fe/activity?state=480&currency=GBP&limit=10&page=1&sort=createdAt&order=DESC&country=GB'
    response = requests.get(page, headers = headers).json()['ProductActivity']
    output_dict = [x for x in response if(x['amount'] == 248)]
    print(output_dict)
    pass

highest_bid()
