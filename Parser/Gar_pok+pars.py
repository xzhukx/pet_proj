from bs4 import BeautifulSoup
import requests as re

web = re.get("https://www.oree.com.ua/")

soup = BeautifulSoup(web.text, features="html5lib")

# # needed_info = soup.find(id="index_col_group")

# # price_type = needed_info.find_all("div", "small-caption pr-1")
# # prices = needed_info.find_all("span", "index-prices-value")
# # countries = needed_info.find_all("div", "index-country-name")


needed_info = soup.find(id="index_col_group")

price_type = needed_info.find_all("div", "small-caption pr-1")
prices = needed_info.find_all("span", "index-prices-value")
countries = needed_info.find_all("div", "index-country-name")

zipped = (price_type, prices, countries)

iter_zip = iter(zipped)

for x in iter_zip:
    print(x)

# найти класс "роу", написать через "next" итератор

