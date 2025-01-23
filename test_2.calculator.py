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

# Ввод в поле delay значение 45  
def delay(self, time: str):
        driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(45)

# Нажатие кнопок 
        driver.find_element(By.XPATH, '//span[text()="7"]').click()
        driver.find_element(By.XPATH, '//span[text()="+"]').click()
        driver.find_element(By.XPATH, '//span[text()="8"]').click()
        driver.find_element(By.XPATH, '//span[text()="="]').click()

# Используем явные ожидания для ожидания появления результата в течение 45 секунд
        waiter=WebDriverWait(driver, 45)
        waiter.until(
             EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#calculator > div.top > div'), '15')  
)

# Проверка результата
        result = WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#calculator > div.top > div'), '15')
    )
        res = "15"
        assert result == res