import requests

headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
url = """https://api.m.jd.com/?appid=www-jd-com&body=%7B%22pin%22%3A%22%22%2C%22uuid%22%3A%22366137340%22%2C%22source%22%3A%22pc-home%22%7D&clientVersion=1.0.0&client=pc&functionId=pc_home_hotwords&screen=&t=1713925366943&uuid=76161171.366137340.1713925284.1713925284.1713925285.1&loginType=3&x-api-eid-token=jdd03BZHPJAO5FDNJ7C7N6JXTEK6NZX6NZBA42HCAVUVRNYLGTSGTMC4KCSI3RHI7VCRBUR7L6CILOEJ2QMFHNZB4BU2FVQAAAAMPBXUHGKAAAAAACKRSTPZUX4GFUMX&callback=jsonpHotWords&_=1713925366995"""
params = {
    "appid": "www-jd-com",
    "body": {"pin": "", "uuid": "366137340", "source": "pc-home"},
    "clientVersion": "1.0.0",
    "client": "pc",
    "functionId": "pc_home_hotwords",
    "screen": "",
    "t": 1713925366943,
    "uuid": "76161171.366137340.1713925284.1713925284.1713925285.1",
    "loginType": "3",
    "x-api-eid-token": "jdd03BZHPJAO5FDNJ7C7N6JXTEK6NZX6NZBA42HCAVUVRNYLGTSGTMC4KCSI3RHI7VCRBUR7L6CILOEJ2QMFHNZB4BU2FVQAAAAMPBXUHGKAAAAAACKRSTPZUX4GFUMX",
    "callback": "jsonpHotWords",
    "_": 1713925366995,
}
resp = requests.get(url)
print(resp.status_code)
