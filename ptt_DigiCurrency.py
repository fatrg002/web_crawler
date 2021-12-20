from bs4 import BeautifulSoup
import requests
url = "https://www.ptt.cc/bbs/DigiCurrency/index428.html"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
titles = soup.find_all('div',class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)