from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.keys import Keys


cookie = {"name": "cookie_policy", "value": "1"}


def test_card_counter():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    # Перейти на сайт «Лабиринта»
    driver.get("https://www.labirint.ru/")
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.add_cookie(cookie)
    # Найти все книги по слову python
    driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')
    driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    # Переключиться на таблицу
    # Добавить все книги на первой странице в корзину и посчитать
    buy_buttons = driver.find_elements(
        By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")

    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    # Перейти в корзину
    driver.get("https://www.labirint.ru/cart/")

    # Проверить счетчик товаров. Должен быть равен числу нажатий
    # Получить текущее значение
    txt = driver.find_element(
        By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, 'b').text

    # Сравнить c counter
    assert counter == int(txt)
    driver.quit()