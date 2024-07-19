import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get("https://opensource-demo.orangehrmlive.com/")
browser.maximize_window()
title = browser.title
print(title)
assert "OrangeHRM" in title
time.sleep(25)
X=browser.find_element(By.NAME,"username")
X.send_keys("Admin")
Y=browser.find_element(By.NAME,"password")
Y.send_keys("admin123")
Z= browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
Z.click()
time.sleep(25)
browser.close()



