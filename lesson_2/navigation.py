import time

from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://yandex.ru")

time.sleep(3)

driver.refresh()