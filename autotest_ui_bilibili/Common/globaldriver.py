from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class GlobalDriver:
    def __init__(self):
        self.driver = None

    def get_driver(self):
        if self.driver is None:
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")

            # 实现浏览器在用例执行完成之后不会关闭    # True: 浏览器不关闭 False: 浏览器关闭
            chrome_options.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(options=chrome_options, service=Service())

            # 修改页面加载策略
            # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出;该行的作用是不等待页面完全加载，立即返回控制权给程序，可提高执行速度，但可能导致获取的内容不完整
            desired_capabilities = DesiredCapabilities.CHROME
            desired_capabilities["pageLoadStrategy"] = "none"

        return self.driver

    def quit_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None


global_driver = GlobalDriver()

# ;只在第一次运行测试时清理 Allure 结果目录，之后不再清理，以保留所有测试结果
# addopts = --alluredir=Outputs/reports/allure_results --clean-alluredir
