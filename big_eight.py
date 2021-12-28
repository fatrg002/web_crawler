import requests
from bs4 import BeautifulSoup
import pandas as pd 
data = []
url ='http://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx'
r = requests.get(url)
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text,'lxml') #parser:html.parser,lxml
    #print(soup.prettify())
    tables = soup.find_all('table',attrs={'cellpadding':'2'})
    for table in tables:
        trs = table.find_all('tr')
        for tr in trs:
            date,value,price = [td.text for td in tr.find_all('td')]
            if date == '日期':
                continue
            data.append([date,value,price])
df = pd.DataFrame(data,columns=['日期','買賣超金額','台指期'] )
df.to_csv('big_eight.csv')
            
