import requests
import json

control = input("İf you want to sort currency, enter 1 ")
if control == "1":
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    response = json.loads(response.text)
    currencies = response['rates']
    for currency in currencies:
        print(currency,end=" ")

pct = input("Enther the pcs : ")
fcurrency = input("Enter the first currency : ")

url = f"https://api.exchangerate-api.com/v4/latest/{fcurrency}"
lcurrency = input("Enter the second currency : ")

try:
    response = requests.get(url)
    jresponse = json.loads(response.text)
    f = float(jresponse['rates'][lcurrency])
    pct = int(pct)
    print(f"{pct} USD = {f*pct} {lcurrency}")
except:
    print("Para birimi aranirken hata alindi.")
finally:
    print("Islem bitmistir.")