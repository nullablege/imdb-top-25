IMDb Top Movies Scraper
This Python script scrapes the top movies from IMDb's Top 250 movies list.

Dependencies:

requests
beautifulsoup4
Setup:

Install the necessary libraries using pip:
pip install requests beautifulsoup4
python imdb_top_movies.py

Script Overview:
The script sends a GET request to IMDb's Top 250 movies page using the requests library.
It then parses the page content with BeautifulSoup.
The script selects movie titles using CSS selectors and prints them to the console.
Note: Make sure to comply with IMDb's scraping policies and terms of service.

IMDb En İyi Filmler Kazıyıcı
Bu Python betiği, IMDb'nin En İyi 250 film listesinden en iyi filmleri kazır.

Gereklilikler:

requests
beautifulsoup4

Kurulum
Gerekli kütüphaneleri pip ile yükleyin:
pip install requests beautifulsoup4
IMDb'den en iyi filmleri almak için betiği çalıştırın:
python imdb_top_movies.py
Betiğin Özeti:

Betik, IMDb'nin En İyi 250 film sayfasına requests kütüphanesi ile GET isteği gönderir.
Sayfa içeriğini BeautifulSoup ile analiz eder.
CSS seçicileri kullanarak film başlıklarını seçer ve konsola yazdırır.
