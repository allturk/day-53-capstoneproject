from bs4 import BeautifulSoup as BS
import requests

headers = {"Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-123.18383254003906%2C%22east%22%3A-122.10442580175781%2C%22south%22%3A37.4100547809968%2C%22north%22%3A38.04762191051941%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'


class ScrapeSite:
    def __init__(self):
        self.report = requests.get(url=url, headers=headers)
        self.site = self.report.text
        self.soup = BS(self.site, "html.parser")

    def find_adresses(self):
        adresses = self.soup.findAll(name="address")
        return adresses

    def find_prices(self):
        pricess = self.soup.findAll(name="div", class_="list-card-price")
        return pricess

    def find_link(self):
        links = self.soup.findAll(name="a", class_="list-card-img")
        return links
