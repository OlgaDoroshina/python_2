from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()


driver.get("https://the-internet.herokuapp.com/entry_ad")

close_button = driver.find_element(By.CSS_SELECTOR, 'div.modal-footer > p')
close_button.click()

sleep(5)

driver.quit()