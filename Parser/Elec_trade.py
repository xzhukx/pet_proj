import requests
import bs4
import re

url="https://www.oree.com.ua/index.php/pricectr"
a=requests.get(url)
print(r.status_code)