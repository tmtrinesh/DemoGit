from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\chromedriver.exe")
driver.get("https://www.google.co.in")
if driver.title == "Google":
    print("test passed")
else:
    print("test failed")

driver.close()
