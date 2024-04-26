import json
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}
url = "https://www.xfz.cn/api/website/home/stream/"
resp = requests.get(url, headers=headers)
json_data = json.loads(resp.text)
print(json_data["data"]["actives"][0])
