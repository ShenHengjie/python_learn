import requests

url = "http://www.baidu.com/s"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}
params = {
    "ie": "utf-8",
    "wd": "python",
}
resp = requests.get(url, params=params, headers=headers)
print(resp.content.decode())
