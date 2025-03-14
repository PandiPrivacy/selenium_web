import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://ru.wikipedia.org')

url = driver.current_url
print('урл страницы = ', url)

current_title = driver.title
print('текущий заголовок =', current_title)

assert url == 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0', 'Ошибка в урле'
assert current_title == 'Википедия — свободная энциклопедия', 'Некорректный залоговок'

print(driver.page_source)
time.sleep(3)
