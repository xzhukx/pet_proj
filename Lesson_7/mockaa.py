# import requests
# import bs4
# import re
#
#
# def find_word_in_article_name():
#     # The website has 356 pages with articles, but I want to take only 10 pages. The reason is faster program usage.
#
#     all_pages = range(1, 11)
#     article_name = []
#     for page in all_pages:
#         url = f'https://texty.org.ua/articles/?page={page}'
#         result = requests.get(url)
#         soup = bs4.BeautifulSoup(result.text, 'lxml')
#
#         for item in soup.select('p'):
#             article_name.append(item.text)
#
#     rep_number = 0
#     reply = 'а'
#
#     for name in article_name:
#         rep_number += len(re.findall(reply, name.lower()))
#     print(article_name)
#     print(f'The number of articles` names is {len(article_name)}.')
#     print(f'The number of {reply} is {rep_number}.')
#
#
# find_word_in_article_name()


import requests
url=requests.get("https://6112b99289c6d00017ac051c.mockapi.io/mockaaa")
print(url)

