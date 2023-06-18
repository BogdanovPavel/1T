import time

# import requests as req
from bs4 import BeautifulSoup
import tqdm
import json
#url = "https://www.avito.ru/all/vakansii?cd=1&q=python"
# https://www.avito.ru/all/vakansii?cd=1&p=1&q=pytho

#resp = req.get(url)
# 1
#print(resp.text)

#soup = BeautifulSoup(resp.text, "lxml")

# 2 поиск по атрибуту
#tag = soup.find(attrs={"data-marker":"page-title/text"})
#print(tag.text)
#print(tag.attrs["class"])

# 3 поиск по тегу
#tag = soup.find_all("a")
#print(tag)

# 4 поиск по классу
#tag = soup.find_all(class_="footer-rubricator-block-jFn8W")
#print(tag)

# 5 поиск по id
#tag = soup.find_all(id_="app")
# print(tag)

# 6 выводим все вакансии со страницы
# tags = soup.find_all(attrs={"data-marker":"item-title"})
# for iter in tags:
#     #print(iter)

# 7
# tags = soup.find_all(attrs={"data-marker":"item-title"})
# for iter in tags:
#     print(iter.text, iter.attrs["href"])

# 8 перебираем данные о вакантсиях сос траницы подборки
#  путем перебота страниц с каждой вакансией
#tags = soup.find_all(attrs={"data-marker":"item-title"})
data = {
    "data":[]
}

from requests_tor import RequestsTor
req = RequestsTor()

for page in range(1, 3):
    url = f"https://www.avito.ru/all/vakansii?cd=1&p=(page)&q=python"
    resp = req.get(url,  headers={"User-Agent":'Mozilla/5.0'})
    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(attrs={"data-marker": "item-title"})
    for iter in tqdm.tqdm(tags):
        time.sleep(2)

        url_object = "https://www.avito.ru" + iter.attrs["href"]
        resp_object = req.get(url_object)

        soup_object = BeautifulSoup(resp_object.text, "lxml")
        tag_price = soup_object.find(attrs={"itemprop":"offers"}).find(attrs={"itemprop":"price"}).text
        # print(iter.text, tag_price)

        tag_region = soup_object.find(attrs={"itemtype":"http://schema.org/ListItem"}).find_all(attrs={"itemprop":"name"})[0].text
        data["data"].append({"Title":iter.text, "Salary":tag_price, "Region":tag_region})
        #print(iter.text, tag_price, tag_region)

        with open("data.json", "w") as file:
            json.dump(data, file, ensure_ascii=False)

#
# for iter in tags:
#     print(iter.text, iter.attrs["href"])
#     url_object = "https://www.avito.ru" + iter.attrs["href"]
#     resp_object = req.get(url_object)
#
#     soup_object = BeautifulSoup(resp_object.text, "lxml")
#     tags = soup.find_all(attrs={"data-marker":"item-title"})