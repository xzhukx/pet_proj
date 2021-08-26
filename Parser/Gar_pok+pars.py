import requests
import bs4

url="https://www.gpee.com.ua/publication?id=1"
a=requests.get(url)
soup = bs4.BeautifulSoup(a.text, "lxml")


text=soup.find_all("h4")
urls=soup.find_all("div", class_="row novost")
print(urls)

content_list=[]
# print(soup.prettify())

# for i in urls:
#     a=i.get("href")
#     print(a)
#
# for j in text:
#     b=j.get_text()
#     print(b)