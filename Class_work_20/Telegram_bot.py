import telebot
import requests as re
from bs4 import BeautifulSoup
import csv

# bot = telebot.TeleBot("2071213971:AAGFlItIZ2doi0p2zD2vRRi3-Px0vR1aw9s", parse_mode=None)
#
# @bot.message_handler(commands=['DAM'])
#
# def send_welcome(message):
# 	bot.reply_to(message, "Hi_man !!!!!!!!")
#
# bot.infinity_polling()

text = re.get("https://www.oree.com.ua")
soup = BeautifulSoup(text.text, "html.parser")
needed_block = soup.find_all('div', 'col-2 mpage-prices index-block')

for content in needed_block:
    country = content.find("div", "index-country-name")

prices_dict = {}


def electr_prices():
    for content in needed_block:
        country = content.find("div", "index-country-name")
        price = content.find("span")
        prices_dict.update({country.text: price.text + " EUR"})
        print(prices_dict)


electr_prices()




    # print(content.find("div", "index-country-name"))
    # print(content.find("span"))


# for h in hh:
#     print(h.parent.find('span'))
#     print(h.find('div','index-country-name'))
#     print(h.find('span'))
# Country_name = soup.find_all("div","index-country-name", "fa fa-sort-down text-danger")
# Prices = soup.find_all("span", "index-prices-value")


# print(Country_name)
# print(Prices)

# POST /index.php/main/get_weighted_average_prices HTTP/1.1
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# Accept: */*
# Accept-Language: en-gb
# Accept-Encoding: gzip, deflate, br
# Host: www.oree.com.ua
# Origin: https://www.oree.com.ua
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15
# Connection: keep-alive
# Referer: https://www.oree.com.ua/
# Content-Length: 48
# Cookie: _ga=GA1.3.1171834215.1633625306; _gat_gtag_UA_144367606_1=1; _gid=GA1.3.199388414.1633625306; PHPSESSID=bbmi9p9oesou5oi0kc0b8faf53
# X-Requested-With: XMLHttpRequest

# with open(newfile, 'wb') as outfile:
#     writer = csv.writer(outfile)
#     writer.writerows(prices_dict.iteritems())
