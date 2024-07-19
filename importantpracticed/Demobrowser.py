from selenium import webdriver

driver = webdriver.Edge()
driver.get("http://rahulshettyacademy.com")
driver.maximize_window()
title = driver.title
print(driver.title)
print(driver.current_url)
driver.close()