import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from Common.globaldriver import global_driver

"""
说明：
由于webdriver的实例化被放在了一个函数或者方法的内部，当这个函数或者方法执行完毕后，由于python的垃圾回收机制，所有的局部变量会被释放，也包括webdriver的实例
所以，如果webdriver实例在函数内部，即使yield后面没有driver.quit()，浏览器也会被关闭
需求：用例执行完成后，浏览器不关闭
两种方法
1.将webdriver的实例化操作放在函数外部，使其成为全局变量，这样即使函数执行完毕，webdriver的实例仍然存在，浏览器也不会关闭（不会因为局部变量的销毁而关闭浏览器）
2.使用特定的选项来控制浏览器的关闭
（1）创建'浏览器选项'对象
（2）使用add_experimental_option方法设置detach选项为True
（3）将chrome_options对象传到浏览器属性中，是detach为True生效
"""


@pytest.fixture(scope="class")
def access_web():
    # # 创建 chrome_options 对象
    # chrome_options = Options()
    # # 设置 detach 选项为 True
    # chrome_options.add_experimental_option("detach", True)
    #
    # # 前置：打开浏览器
    # # 修改页面加载策略
    # desired_capabilities = DesiredCapabilities.CHROME
    # # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出;该行的作用是不等待页面完全加载，立即返回控制权给程序，可提高执行速度，但可能导致获取的内容不完整
    # desired_capabilities["pageLoadStrategy"] = "none"
    #
    # # 较新的 Selenium 版本中，推荐使用 Service 类来管理 WebDriver 的服务
    # driver = webdriver.Chrome(options=chrome_options, service=Service())
    # driver.get("https://passport.bilibili.com/login")
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    #
    # # 返回对象
    # yield driver
    # # 后置：关闭浏览器
    # # driver.quit()
    driver = global_driver.get_driver()
    driver.get("https://passport.bilibili.com/login")
    # driver.implicitly_wait(10)

    # 返回对象
    yield driver
    # 后置：关闭浏览器
    # driver.quit()


@pytest.fixture
def refresh_web(access_web):
    yield access_web
    # 刷新页面
    access_web.refresh()
    time.sleep(1)


def pytest_configure(config):
    config.addinivalue_line("markers", 'smoke')
    config.addinivalue_line("markers", 'P0')
    config.addinivalue_line("markers", 'P1')
