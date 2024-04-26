from email import header
import json
import requests
import time

f = open("TX招聘.json", "a", encoding="utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}
url = "https://careers.tencent.com/tencentcareer/api/post/Query"
for i in range(1, 98):
    params = {
        "timestamp": time.time(),
        "categoryId": "40001001,40001002,40001003,40001004,40001005,40001006",
        "attrId": 1,
        "pageIndex": i,
        "pageSize": 10,
        "language": "zh-cn",
        "area": "us",
    }
    resp = requests.get(url, params=params, headers=headers)
    resp.encoding = "utf8"
    resp_json = resp.json()
    # print(resp_json)
    # with open("TX招聘.json", "w", encoding="utf-8") as f:
    #     f.write(json.dumps(resp_json, ensure_ascii=False))
    # 获取所有的岗位数据
    Posts = resp_json["Data"]["Posts"]
    # 遍历所有岗位数据
    for item in Posts:
        # print(item)
        f.write(json.dumps(item, ensure_ascii=False) + ",")
f.close()
