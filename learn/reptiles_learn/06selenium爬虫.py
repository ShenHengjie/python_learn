import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
url = "https://liuyan.people.com.cn/login"
driver.get(url)
driver.maximize_window()
html = driver.page_source
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div[1]/div[2]/main/form/div[1]/div/div/input").send_keys("17796869859")
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div[1]/div[2]/main/form/div[2]/div/div/input").send_keys("aaaaaaaaaa")
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div[1]/div[2]/main/form/div[3]/div/button").click()
time.sleep(10)
driver.quit()

