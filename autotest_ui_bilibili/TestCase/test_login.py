import allure
import os
import pytest

from PageObjects.bilibili_login_page import BilibiliLoginPage

# 获取当前文件所在目录
root = os.path.dirname(os.path.abspath(__file__))


# @allure.feature("模块：b站登录")
class TestChannel:

    # @pytest.mark.P1
    # @allure.story("正向登录测试")
    def test_bilibili_login(self, refresh_web):
        """
        b站登录模块正向测试
        """
        # result_text = bp(refresh_web).webstar()
        # assert result_text != "登录"
        bp = BilibiliLoginPage(refresh_web)
        page_title = bp.login_process()
        assert page_title == "哔哩哔哩 (゜-゜)つロ 干杯~-bilibili"
