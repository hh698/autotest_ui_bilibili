import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.bilibili.com')
driver.maximize_window()
time.sleep(3)
# driver.quit()
