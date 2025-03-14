import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://yandex.ru/maps/')

driver.find_element('xpath', '//input[contains(@class, \'input__control\') and contains(@class, \'_bold\')]').click()

time.sleep(3)
