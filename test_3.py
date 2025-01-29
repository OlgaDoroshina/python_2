from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from classes import LoginPage, ProductsPage, CheckoutPage, PersonalInfoPage, OverviewPage


def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_complete_purchase(driver):
    saucedemo_url = "https://www.saucedemo.com/"

    # Шаг 1: Создание страниц
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    checkout_page = CheckoutPage(driver)
    personal_info_page = PersonalInfoPage(driver)
    overview_page = OverviewPage(driver)

    # Шаг 2: Авторизация
    login_page.login_as_standard_user()

    # Шаг 3: Добавление товаров в корзину
    products_page.add_products_to_cart("Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie")

    # Шаг 4: Переход в корзину
    products_page.go_to_shopping_cart()

    # Шаг 5: Оформление заказа
    checkout_page.proceed_to_checkout()

    # Шаг 6: Заполнение персональной информации
    personal_info_page.fill_personal_info("Andrey", "B", "123")

    # Шаг 7: Проверка итоговой стоимости и завершение покупки
    total_amount = overview_page.get_total_amount()
    assert total_amount == "58.29", f"Expected '58.29', but got {total_amount}"

    overview_page.complete_purchase()