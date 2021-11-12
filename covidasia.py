import requests
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/#countries'
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

r = requests.get(url)
asia = []
info = []
soup = BeautifulSoup(r.text,"html.parser")
info = soup.findAll('tr',class_='row_continent total_row')


print(info)




