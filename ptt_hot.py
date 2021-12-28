import requests
from bs4 import BeautifulSoup

root_url = 'https://disp.cc/b/'
r = requests.get('https://disp.cc/b/PttHot')
soup = BeautifulSoup(r.text,'html.parser')

#----------version1----------------------
#spans = soup.find_all('span',class_='listTitle')

#for span in spans:
    
#    href = span.find('a').get('href')
#    if href == '796-59l9': #把開版成功去除
#        break
#    url = root_url + href
#    title = span.text
    
#    print(f'{title}\n{url}')


#----------------version2 use css select-------------------
for span in soup.select('#list span.listTitle'):
    href = span.find('a').get('href')
    if href == '796-59l9': 
        break
    
    url  = root_url + href
    title = span.text
    
    print(f'{title}\n{url}')
    
