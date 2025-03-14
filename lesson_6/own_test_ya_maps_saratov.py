# якарты уносят меня в казахстан
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Переход на Яндекс.Карты
driver.get('https://yandex.ru/maps/')

time.sleep(3)

# Клик и вводу в поиск Саратов
poisk = driver.find_element("xpath", "//input[contains(@class, 'input__control _bold')]")
poisk.click()
poisk.send_keys("Саратов")

# Проверка того, что текст введен в поле
assert poisk.get_attribute("value")

time.sleep(3)

# Клик по первому варианту
pervii_variant = driver.find_element("xpath", "(//div[contains(@class, 'suggest-item-view')])[1]")
pervii_variant.click()

time.sleep(3)

# Ожидание загрузки элемента <ymaps>
ymaps_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//ymaps[contains(@class, 'ymaps3x0--map')]"))
)

# Получить атрибут style элемента
style_value = ymaps_element.get_attribute("style")

# Проверить соответствие атрибута style
expected_style = "width: 431px; height: 1252px; touch-action: none;"
if style_value == expected_style:
    print("Стиль элемента <ymaps> соответствует ожидаемому.")
else:
    print("Стиль элемента <ymaps> не соответствует ожидаемому.")
    print(f"Найденный стиль: {style_value}")

# Ожидание загрузки элементов
toponym_cards_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'toponym-card-discovery-carousel__label')]"))
)

# Проверить количество элементов
expected_count = 3
actual_count = len(toponym_cards_elements)

if actual_count == expected_count:
    print(f"Количество элементов корректно: {actual_count}.")
else:
    print(f"Количество элементов некорректно: {actual_count}.")

# Проверка названий элементов
expected_titles = ["Чем заняться", "Где поесть", "Подборки"]
actual_titles = [label.text for label in toponym_cards_elements]

for expected, actual in zip(expected_titles, actual_titles):
    if expected == actual:
        print(f"Название '{actual}' соответствует ожидаемому.")
    else:
        print(f"Название '{actual}' не соответствует ожидаемому. Ожидалось: '{expected}'.")

# Выход
driver.quit()
