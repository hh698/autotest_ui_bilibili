import time

from selenium import webdriver

# driver = webdriver.Chrome()
driver = webdriver.Chrome(
    executable_path=r'C:\Users\gd12773-hlw\AppData\Local\Programs\Python\Python310\chromedriver.exe')
driver.get('https://www.bilibili.com')
driver.maximize_window()
time.sleep(1)
driver.quit()
