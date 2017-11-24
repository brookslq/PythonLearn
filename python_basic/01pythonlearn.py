#coding=utf-8

from bs4 import BeautifulSoup
import requests




def star():
    urls = ['http://www.guazi.com/tj/buy/o{}/'.format(str(i)) for i in range(1, 30, 1)]
    for url in urls:
        detailOper(url)


def detailOper(url):
    print (url)



