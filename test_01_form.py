import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
 
# Фикстура для создания WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()
 
# Тест
def test_01_form(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
 
    # Заполнение формы
    first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
    first_name.clear()
    first_name.send_keys("Иван")
 
    last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
    last_name.clear()
    last_name.send_keys("Петров")
 
    address = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
    address.clear()
    address.send_keys("Ленина, 55-3")
 
    email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
    email.clear()
    email.send_keys("test@skypro.com")
 
    phone_number = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
    phone_number.clear()
    phone_number.send_keys("+7985899998787")
 
    zip_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
    zip_code.clear()
    zip_code.send_keys("")
 
    city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
    city.clear()
    city.send_keys("Москва")
 
    country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
    country.clear()
    country.send_keys("Россия")
 
    job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
    job_position.clear()
    job_position.send_keys("QA")
 
    company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
    company.clear()
    company.send_keys("SkyPro")
 
    # Нажатие на кнопку
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
 
    # Проверка красного поля
    alert_danger_color = "rgba(248, 215, 218, 1)"
    color_zip = zip_code.value_of_css_property("background-color")
    assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"
 
    # Проверка зеленого поля
    alert_success_color = "rgba(209, 231, 221, 1)"
    fields = [first_name, last_name, address, email, phone_number, city, country, job_position, company]
    for field in fields:
        field_color = field.value_of_css_property("background-color")
        assert field_color == alert_success_color, f"Expected {alert_success_color} for {field.get_attribute('name')}, but got {field_color}"