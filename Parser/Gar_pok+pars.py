import requests
import bs4

url="https://www.gpee.com.ua/publication?id=1"
a=requests.get(url)
soup = bs4.BeautifulSoup(a.text, "lxml")


text=soup.find_all("h4", style_="margin-left:10px; ")
urls=soup.find_all("form", class_="choose_new")
print(urls)

# print(urls)
# content_list=[]
# print(soup.prettify())

# for i in urls:
#     a=i.get("href")
#     print(a)
#
# for j in text:
#     b=j.get_text()
#     print(b)