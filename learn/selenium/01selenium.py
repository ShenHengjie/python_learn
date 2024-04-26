from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.csdn.net/")
driver.maximize_window()
driver.get("https://blog.csdn.net/qq_43965708")
driver.back()
driver.forward()
