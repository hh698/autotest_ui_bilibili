import time

import allure
import os
import pytest
from Common.basepage import BasePage as BP
from PageObjects.bilibili_login_page import BilibiliLoginPage
from PageObjects.read_loginyaml import ReadLoginYaml

# 获取当前文件所在目录
root = os.path.dirname(os.path.abspath(__file__))


@allure.feature("模块：b站登录")
class TestChannel:
    @pytest.mark.smoke
    @allure.severity(severity_level="[normal]")
    @allure.story("正向登录测试，账号密码均正确")
    def test_bilibili_login1(self, access_web):
        screenshot_dir = "../Outputs/assert_screenshots"
        with allure.step("步骤1：登录"):
            self.reader = ReadLoginYaml()  # 创建 ReadLoginYaml 的实例
            phone_number = self.reader.get_phone_number()
            phone_password = self.reader.get_phone_password()
            bp = BilibiliLoginPage(access_web)  # 传递refresh_web得到的driver
            page_title = bp.login_process(phone_number, phone_password)
            with allure.step("步骤2：断言"):
                try:
                    assert page_title == "登录验证1"
                    print("断言成功，页面标题正确！")
                    BP.take_screenshot(access_web, "login_page.png", screenshot_dir)
                except AssertionError as e:
                    print("断言失败，页面标题错误！")
                    BP.take_screenshot(access_web, "login_page_error.png", screenshot_dir)

        # assert page_title == "哔哩哔哩 (゜-゜)つロ 干杯~-bilibili"

    @pytest.mark.P0
    @allure.severity(severity_level="[normal]")
    @allure.story("逆向登录测试，账号错误，密码正确")
    def test_bilibili_login2(self, access_web):
        with allure.step("步骤1：登录"):
            # time.sleep(3)
            self.reader = ReadLoginYaml()  # 创建 ReadLoginYaml 的实例
            phone_number = self.reader.get_phone_number_2()
            phone_password = self.reader.get_phone_password_2()
            bp = BilibiliLoginPage(access_web)  # 传递refresh_web得到的driver
            page_title = bp.login_process(phone_number, phone_password)
        with allure.step("步骤2：断言"):
            assert page_title == "账号登录"
            # assert page_title == "哔哩哔哩 (゜-゜)つロ 干杯~-bilibili"

    # @pytest.mark.smoke
    # @allure.severity(severity_level="[normal]")
    # @allure.story("逆向登录测试，账号正确，密码错误")
    # def test_bilibili_login3(self, refresh_web):
    #     with allure.step("步骤1：登录"):
    #         self.reader = ReadLoginYaml()  # 创建 ReadLoginYaml 的实例
    #         phone_number = self.reader.get_phone_number_3()
    #         phone_password = self.reader.get_phone_password_3()
    #         bp = BilibiliLoginPage(refresh_web)  # 传递refresh_web得到的driver
    #         page_title = bp.login_process(phone_number, phone_password)
    #     with allure.step("步骤2：断言"):
    #         assert page_title == "账号登录"
    # assert page_title == "哔哩哔哩 (゜-゜)つロ 干杯~-bilibili"

    # @pytest.mark.smoke
    # @allure.severity(severity_level="[normal]")
    # @allure.story("逆向登录测试，账号密码均错误")
    # def test_bilibili_login4(self, refresh_web):
    #     with allure.step("步骤1：登录"):
    #         self.reader = ReadLoginYaml()  # 创建 ReadLoginYaml 的实例
    #         phone_number = self.reader.get_phone_number_4()
    #         phone_password = self.reader.get_phone_password_4()
    #         bp = BilibiliLoginPage(refresh_web)  # 传递refresh_web得到的driver
    #         page_title = bp.login_process(phone_number, phone_password)
    #     with allure.step("步骤2：断言"):
    #         assert page_title == "账号登录"
    # assert page_title == "哔哩哔哩 (゜-゜)つロ 干杯~-bilibili"


"""
新增一个错误的账号密码登录的用例，思路：
去掉bilibili_login_page中的login_process，直接调用webstar方法，传入username和password参数
这个过程在测试用例里面完成，让测试用例直接控制传参

对webstar方法进行修改，其中直接调用pass_touclick方法

同时对第一个用例也进行修改
"""

# if __name__ == '__main__':
#     pytest.main(["-s", "-v", "test_login.py"])
#     os.system("allure generate Outputs/reports/allure-results -o Outputs/reports/allure-report --clean")
# pytest.main(
#     [["-s", "-v", "-m", "sj", "--html=Outputs/report/pytest.html", "--alluredir=Outputs/reports/allure-results"],
#      "test_login.py"])
