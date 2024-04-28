from ast import main
import time
from tkinter.tix import MAIN
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# 后台启动
option = webdriver.EdgeOptions()
option.add_argument("headless")
driver = webdriver.Edge(option)
# 前台启动
# driver = webdriver.Edge()
url = "https://liuyan.people.com.cn/index"
driver.get(url)
driver.maximize_window()
html = driver.page_source
# driver.find_element(
#     By.XPATH,
#     "/html/body/div[1]/div[2]/main/div/div/div/div[1]/div[2]/main/form/div[1]/div/div/input",
# ).send_keys("17796869859")
# driver.find_element(
#     By.XPATH,
#     "/html/body/div[1]/div[2]/main/div/div/div/div[1]/div[2]/main/form/div[2]/div/div/input",
# ).send_keys("aaaaaaaaaa")
# driver.find_element(
#     By.XPATH,
#     "/html/body/div[1]/div[2]/main/div/div/div/div[1]/div[2]/main/form/div[3]/div/button",
# ).click()
li_list = driver.find_elements(
    By.XPATH, "/html/body/div[1]/div[2]/main/div/div/div[2]/div[2]/div/ul/li"
)
print("============================")
# print(len(ul_list))
data = []
for item in li_list:
    apartment = item.find_element(By.XPATH, "./h1")
    apartment_position = item.find_element(By.XPATH, "./h2")
    leader_name = item.find_element(By.XPATH, './div/p[@class="leaderNameInfo"]')
    data.append(
        {
            "apartment": apartment.text,
            "apartment_position": apartment_position.text,
            "leader_name": leader_name.text,
        }
    )
driver.quit()
print(data)


def pd_toExcel(data, fileName):
    apartments = []
    apartment_positions = []
    leader_names = []
    for i in range(len(data)):
        apartments.append(data[i]["apartment"])
        apartment_positions.append(data[i]["apartment_position"])
        leader_names.append(data[i]["leader_name"])
    df = pd.DataFrame(
        {
            "apartment": apartments,
            "apartment_position": apartment_positions,
            "leader_name": leader_names,
        }
    )
    df.to_excel(f"{fileName}.xlsx", index=False)


pd_toExcel(data, "testData")
