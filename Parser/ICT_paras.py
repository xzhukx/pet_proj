import requests
import bs4

url="https://itc.ua"
a=requests.get(url)
soup = bs4.BeautifulSoup(a.text, "lxml")
# print(soup.prettify())

urls=soup.find_all("a")
content_list=[]

for i in urls:
    a=i.get("href")
    b=i.get_text()
    content_list.append(str(a)+" "+str(b))
    print(content_list)