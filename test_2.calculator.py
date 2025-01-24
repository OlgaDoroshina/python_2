import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Тест
@pytest.fixture
def driver():
   driver = webdriver.Chrome()
   yield driver
   driver.quit()

def result(self):
        end_result = self._driver.find_element(By.CSS_SELECTOR, '#calculator > div.top > div').text
        return end_result

# Зайти на сайт 
def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Установка задержки
    delay_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay"))
    )
    delay_field.clear()
    delay_field.send_keys("45")

    # Нажатие кнопок
    buttons = ["7", "+", "8", "="]
    for button in buttons:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//span[text()="{button}"]'))
        ).click()

    # Ожидание результата
    result = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#calculator > div.top > div"), "15")
    )
    assert result, "Результат не совпадает с ожидаемым: 15"