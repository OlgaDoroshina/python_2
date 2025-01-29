from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from calculator_page import CalculatorPage
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_calculator(driver):
    calculator_page = CalculatorPage(driver)
    calculator_page.open_page("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calculator_page.enter_delay_value("45")
    calculator_page.click_button("7")
    calculator_page.click_operator_button("+")
    calculator_page.click_button("8")
    calculator_page.click_equals_button()

    # Ожидание перед извлечением результата
    result = calculator_page.get_result_text()

    # Прямой поиск элемента и извлечение текста
    result_element = driver.find_element(By.CSS_SELECTOR, "div.screen")
    result = result_element.text.strip()

    # Добавить ожидание перед извлечением результата
    ChromeDriverManager(driver, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))

    # Проверка результата
    result_element = driver.find_element(By.CSS_SELECTOR, "div.screen")
    result = result_element.text.strip()
    assert result == "15"