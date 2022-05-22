from scraping_site import ScrapeSite
from fill_form import FillForm

bs = ScrapeSite()
adresses = bs.find_adresses()
adress_list = []
for adres in adresses:

    adress_list.append(adres.text)
prices = bs.find_prices()
price_list = []
for price in prices:
    price_list.append((price.text.split("+"))[0].strip("/mo"))
links = bs.find_link()
link_list = []
for link in links:
    if "https://" in link.get("href"):
        link_list.append(link.get("href"))
    else:
        link_list.append(f'https://www.zillow.com/{link.get("href")}')

myform = FillForm()
for n in range(len(adress_list)):
    addr = adress_list[n]
    prc = price_list[n]
    lnk = link_list[n]
    myform.fill_form(addr, prc, lnk)
