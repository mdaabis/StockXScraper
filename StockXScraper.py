import requests
from bs4 import BeautifulSoup
from decouple import config
import json
import pandas as pd
# from stockxsdk import Stockx
import datetime
from datetime import date

email = config('EMAIL')
password = config('PASSWORD')
url = 'https://stockx.com/api/products/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}


def recent_sales():
    page = url + '5e6a1e57-1c7d-435a-82bd-5666a13560fe/activity?state=480&currency=GBP&limit=1000&page=1&sort=createdAt&order=DESC&country=GB'
    cut_off_date = date.today() - datetime.timedelta(0)

    response = requests.get(page, headers = headers).json()['ProductActivity']
    size_filtered_sales = [x for x in response if(x['shoeSize'] == '10')]
    date_filtered_sales = [x for x in size_filtered_sales if (datetime.datetime.strptime(x['createdAt'][:10], "%Y-%m-%d").date() >= cut_off_date)]

    # print(date_filtered_sales)
    # with open('data.txt', 'w') as outfile:
    #     json.dump(date_filtered_sales, outfile)
    pass



recent_sales()
