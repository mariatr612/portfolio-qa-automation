from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://www.google.com")

import time
time.sleep(3)
driver.quit()
