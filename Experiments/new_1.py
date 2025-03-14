import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Переход на Яндекс.Карты
    driver.get('https://yandex.ru/maps/')

    # Ожидание загрузки поля поиска и взаимодействие с ним
    wait = WebDriverWait(driver, 10)
    poisk = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@class, 'input__control')]")))
    poisk.click()
    poisk.send_keys("Саратов")

    # Проверка того, что текст введен в поле
    assert poisk.get_attribute("value") == "Саратов", "Текст в поле не соответствует ожидаемому значению"

    # Ожидание и выбор первого предложения
    pervii_variant = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'suggest-item-view')])[1]")))
    pervii_variant.click()

    # Дополнительная пауза для наблюдения, если необходимо
    time.sleep(3)

finally:
    # Закрытие драйвера
    driver.quit()
