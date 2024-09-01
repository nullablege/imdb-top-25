import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content,"html.parser")
filmler = soup.select("h3.ipc-title__text")

for film in filmler:
    print(film.text)