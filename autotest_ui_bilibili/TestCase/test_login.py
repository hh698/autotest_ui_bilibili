import allure
import os
import pytest

from PageObjects.bilibili_login_page import BilibiliLoginPage

# 获取当前文件所在目录
root = os.path.dirname(os.path.abspath(__file__))


@allure.feature("模块：b站登录")
class TestChannel:

    @pytest.mark.smoke
    @allure.severity(severity_level="[normal]")
    @allure.story("正向登录测试")
    def test_bilibili_login(self, refresh_web):
        """
        b站登录模块正向测试
        """
        # result_text = bp(refresh_web).webstar()
        # assert result_text != "登录"
        with allure.step("步骤1：登录"):
            bp = BilibiliLoginPage(refresh_web)  # 传递refresh_web得到的driver
            page_title = bp.login_process()
        with allure.step("步骤2：断言"):
            # assert page_title == "登录验证"
            assert page_title == "哔哩哔哩 (゜-゜)つロ 干杯~-bilibili"


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
