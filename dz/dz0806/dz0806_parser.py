import json

import requests
from bs4 import BeautifulSoup
import csv


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    # Сайт 1  TXT
    def parsing(self):
        news = self.html.find_all("article", class_="col-md-4 topic topic-thumbnail topic-type-topic")
        for item in news:
            title = item.find("h3").text
            category = item.find("li", class_="topic-info-type").text.strip()
            date = item.find("li", class_="topic-info-date").text.strip()
            blog = item.find("li", class_="topic-info-blog").text.strip()


            self.res.append({
                "title": title,
                "category": category,
                "date": date,
                "blog": blog
            })

        print(self.res)

    def save(self):
        with open(self.path, "w") as f:
            i = 1
            for item in self.res:
                f.write(f"Новость № {i}\n\nНазвание: {item['title']}\n\nКатегория: {item['category']}\n\nДата:"
                        f" {item['date']}\n\nРаздел блога: {item['blog']}\n\n{'*' * 50}\n")
                i += 1

    # Сайт 2  CSV
    # def parsing(self):
    #     concerts = self.html.find_all("div", itemtype="http://data-vocabulary.org/Event")
    #     for item in concerts:
    #         time = item.find("div", class_="time").text
    #         title = item.find("span", itemprop="summary").text
    #         place = item.find("div", class_="place").text
    #
    #         self.res.append({
    #             "Время": time,
    #             "Спектакль": title,
    #             "Место": place
    #         })
    #
    #     print(self.res)
    #
    # def write_csv(self):
    #     with open(self.path, 'w', encoding="utf-8-sig") as f:
    #         writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=self.res[0].keys())
    #         writer.writeheader()
    #         for d in self.res:
    #             writer.writerow(d)

    # Сайт 3  JSON
    # def parsing(self):
    #     store = self.html.find_all("div", class_="product-item")
    #     for item in store:
    #         price = item.find("div", class_="product-item-price__act body-price-primary").text.strip()
    #         name = item.find("a", class_="product-item__name body-list-header").text.strip()
    #
    #         self.res.append({
    #             "price": price,
    #             "name": name
    #         })
    #
    #     print(self.res)

    # def dump_to_json(self):
    #     with open(self.path, 'w', encoding="utf-8") as f:
    #         json.dump(self.res, f, indent=4)
    #
    # def read_json(self):
    #     with open(self.path, "r") as f:
    #         print(json.load(f))

    def run(self):
        self.get_html()
        self.parsing()
        #  Сайт 1
        self.save()
        #  Сайт 2
        # self.write_csv()
        #  Сайт 3
        # self.dump_to_json()
        # self.read_json()
