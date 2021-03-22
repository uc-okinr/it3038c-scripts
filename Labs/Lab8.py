from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://cech.uc.edu/programs.html').content
soup = BeautifulSoup(r, "lxml")
print(type(soup))
print(soup.prettify()[:100])



for link in soup.find_all('a'):
    print(link.get('title'))
    