from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

soup = BeautifulSoup("https://www.gpee.com.ua/publication?id=1", "lxml")
print(soup)



last_heigh=browser.execute_script("https://www.gpee.com.ua/assets/js/news/get_more_news.js?v=82")
print(last_heigh)