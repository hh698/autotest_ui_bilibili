from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# 创建 Chrome 选项
chrome_options = Options()
chrome_options.add_experimental_option("detach", False)

# 初始化 WebDriver 实例
driver = webdriver.Chrome(options=chrome_options, service=Service())

# 打开一个网页
driver.get("https://www.baidu.com")

# 等待一段时间

time.sleep(3)
