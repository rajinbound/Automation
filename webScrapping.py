import requests
from bs4 import BeautifulSoup

li = []
data = requests.get("https://www.imdb.com/find?s=ep&q=thriller&ref_=nv_sr_sm")
soup = BeautifulSoup(data.content,'html.parser')
#print(soup.prettify())
moviesTable = soup.find('table',{'class':'findList'})
#print(moviesTable.prettify())
rows = moviesTable.findAll('tr')
for row in rows:
    rowdata = row.findAll('td')
    #print(rowdata[1].a.text)
    subUrl =rowdata[1].a['href']
    subdata = requests.get("https://www.imdb.com"+subUrl)
    childSoup = BeautifulSoup(subdata.content, 'html.parser')
    if childSoup.find('div',{'class':'see-more inline canwrap'}):
        genre =childSoup.find('div',{'class':'see-more inline canwrap'})
        if genre.a.text == " Documentary":
            print(rowdata[1].a.text)
            print(genre.a.text)
            li.append(rowdata[1].a.text)

print(li)

















