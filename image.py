import urllib
from bs4 import BeautifulSoup

print('Beginning file download with urllib2...')

url = 'http://soloist.co.kr/shop/shopdetail.html?branduid=673563&xcode=060&mcode=004&scode=&special=6&GfDT=bm11W10%3D'

req = urllib.request.Request(url)
res = urllib.request.urlopen(url).read()

soup = BeautifulSoup(res, 'html.parser')
# soup = soup.find("div",class_="poster")

imgUrl = soup.select("img")

for item in imgUrl:
    temp = item['src']
    print(temp)
    if temp[0:5] == "http:":
        urllib.urlretrieve(temp, 'download/' + item['src'].split("/")[-1])
        print(item['src'].split("/")[-1])
