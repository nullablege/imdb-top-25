from bs4 import BeautifulSoup
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}
url = "https://www.akakce.com/arama/?"


query = []
print("Aramak istediginiz kelimeyi girin : ")
secenek = input("Arama kelimesi :")
query.append(f"q={secenek}")
print("Max fiyat gir : ( İstemiyorsan 0 Gir .)")
secenek = input("Max fiyat :")
if not secenek == "0":
    query.append(f"p2={secenek}")

print("Min fiyat gir : ( İstemiyorsan 0 Gir .)")
secenek = input("Min fiyat :")
if not secenek == "0":
    query.append(f"p1={secenek}")

print("Siralama elemani ( İstemiyorsan 0 ) gir \n1.)Populerlik\n2.)En Dusuk Fiyat\n3.)En Yeni\n4.)En Yuksek Fiyat\n5.)En Yuksek Puan")
if secenek == "1":
    query.append(f"s=1")
elif secenek == "2":
    query.append(f"s=2")
elif secenek == "3":
    query.append(f"s=3")
elif secenek == "4":
    query.append(f"s=4")
elif secenek == "5":
    query.append(f"s=7")

if len(query)>1:
    query_str = "&".join(query)
    url = url + query_str
else:
    url = url+query[0]

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
lis = soup.find(id="APL").find_all('li')
for li in lis:
    print("\n")
    print(li.select('h3.pn_v8')[0].text,"\nKargo Dahil En Ucuz : \n",li.select('span.pt_v9')[0].text)
    