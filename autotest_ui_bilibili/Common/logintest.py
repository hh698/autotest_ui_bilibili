from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 创建 chrome_options 对象
chrome_options = Options()
# 设置 detach 为 True，让测试完成后浏览器不关闭
chrome_options.add_experimental_option("detach", True)

# 创建浏览器实例
driver = webdriver.Chrome(options=chrome_options, service=Service())
url = "https://www.baidu.com"
driver.get(url)
driver.maximize_window()

