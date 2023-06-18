import time
import requests as req
from bs4 import BeautifulSoup
import tqdm
import json

data = {
    "data":[]
}
#
# from requests_tor import RequestsTor
# req = RequestsTor()

for page in range(0, 3):
    #url = f"https://www.avito.ru/all/vakansii?cd=1&p=(page)&q=python"
    url = f"https://tyumen.hh.ru/search/vacancy?no_magic=true&L_save_area=true&text=python+разработчик&excluded_text=&area=113&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&page=0"
    resp = req.get(url, headers={"User-Agent":'Mozilla/5.0'})
    soup = BeautifulSoup(resp.text, "lxml")

    tags = soup.find_all(attrs={"data-qa": "serp-item__title"})
    #print(tags)

    for iter in tqdm.tqdm(tags):

        time.sleep(2)

        url_object = iter.attrs["href"]
        resp_object = req.get(url_object)

        soup_object = BeautifulSoup(resp_object.text, "lxml")
        tag_price = soup_object.find(attrs={"itemprop":"offers"}).find(attrs={"itemprop":"price"}).text

        tag_region = soup_object.find(attrs={"itemtype":"http://schema.org/ListItem"}).find_all(attrs={"itemprop":"name"})[0].text
        data["data"].append({"Title":iter.text, "Salary":tag_price, "Region":tag_region})

        with open("data1.json", "w") as file:
            json.dump(data, file, ensure_ascii=False)
