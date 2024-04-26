import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}
resp = requests.get("https://books.toscrape.com/", headers=header)
content = resp.text
soup = BeautifulSoup(content, "html.parser")
all_prices = soup.find_all("p", attrs={"class": "price_color"})
# 找价格
# for price in all_prices:
#     print(price.string[2:])
# 找书名
all_titles = soup.find_all("h3")
for title in all_titles:
    all_links = title.find_all("a")
    for link in all_links:
        print(link.string)
