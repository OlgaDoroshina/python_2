from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/entry_ad")

wait = WebDriverWait(driver, 10)
modal = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.modal")))


close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.modal-footer > p')))
close_button.click()

driver.quit()