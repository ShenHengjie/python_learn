import requests

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}
resp = requests.get("https://books.toscrape.com/", headers=head)
if resp.ok:
    print(resp.text)
else:
    print("error!")
with open("books.html", "w", encoding="utf-8") as f:
    f.write(resp.content.decode("utf-8"))
# url = "http://httpbin.org/post"
# reponse = requests.post(url)
# print(reponse.text)
# url = "https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php"
# data = {
#     "log": "ceshi",
#     "pwd": "admin123456",
#     "wp-submit": "登录",
#     "redirect_to": "https://wordpress-edu-3autumn.localprod.oc.forchange.cn",
#     "testcookie": "1",
# }
# r = requests.post(url, data=data, headers=head)
# r.encoding = "utf8"
# print(r.text)
