import requests
from bs4 import BeautifulSoup

li = []
data = requests.get("https://www.audiotelligence.com/careers/")
soup = BeautifulSoup(data.content,'html.parser')
print(soup.prettify())
appium = soup.find('a',string='canonical')
print(appium['href'])


