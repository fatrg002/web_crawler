from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.ptt.cc/bbs/movie/index9503.html")
soup = BeautifulSoup(r.text,"html.parser")
titles  = soup.find_all('div',class_ = 'title')
print(titles)

for title in titles:
    if title.a != None:
        print(title.a.string)

