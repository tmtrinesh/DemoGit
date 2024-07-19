from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C://Program Files/Google/Chrome/chromedriver.exe")
driver.get("https://www.google.com/maps/@12.9983818,77.5517653,13z")
sleep(2)


def searchplace():
    place = driver.find_element(By.CLASS_NAME,"tactile-searchbox-input")
    place.send_keys("Davanagere")
    submit = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")

    submit.click()


searchplace()


def directions():
    sleep(10)
    direction = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button")
    direction.click()


directions()


def find():
    sleep(6)
    bind = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]"
                                        "/div[1]/div/input")
    bind.send_keys("Harihar")
    sleep(6)
    search = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/"
                                          "div[1]/div[2]/button[1]")
    search.click()


find()


