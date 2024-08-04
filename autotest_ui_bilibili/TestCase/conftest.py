import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="class")
def access_web():
    # 前置：打开浏览器
    # 修改页面加载策略
    desired_capabilities = DesiredCapabilities.CHROME
    # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出;该行的作用是不等待页面完全加载，立即返回控制权给程序，可提高执行速度，但可能导致获取的内容不完整
    desired_capabilities["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome()
    driver.get("www.bilibili.com")
    driver.maximize_window()
    time.sleep(4)
    # 返回对象
    yield driver
    # 后置：关闭浏览器
    driver.quit()

    @pytest.fixture
    def refresh_web(access_web):
        yield access_web
        # 刷新页面
        access_web.refresh()
        time.sleep(1)
