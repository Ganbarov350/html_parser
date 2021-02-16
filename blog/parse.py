from bs4 import BeautifulSoup
import requests


def parser(url):
    if "www.trendyol.com" in url:
        r = requests.get(url=url)
        soup = BeautifulSoup(r.content,'lxml')
        price = soup.find('span',attrs={'class':"prc-slg"}).text
        image = soup.find('img',attrs={"class": "ph-gl-img"})['src']
        return image, price

    image = None
    price = None
    return image, price

