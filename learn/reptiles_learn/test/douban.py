from turtle import title
import requests
from lxml import etree
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}
for i in range(0, 250, 25):
    resp = requests.get(f"https://movie.douban.com/top250?start={i}", headers=headers)
    # with open("douban.html", "w", encoding="utf-8") as f:
    #     f.write(resp.content.decode())
    print(resp)
    page = resp.text
    html = etree.HTML(page)
    titles_chinese = html.xpath(
        """/html/body/div[3]/div[1]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()"""
    )
    scores = html.xpath("//*[@class='rating_num'][1]/text()")
    comments_num = html.xpath("//*[@class='star']/span[4]/text()")
    for title, score, comments in zip(titles_chinese, scores, comments_num):
        print("名称:" + title + " " + "得分" + score + " " + "评论人数" + comments)
    time.sleep(2)
