import allure
import os
import pytest

from PageObjects.bilibili_login_page import BilibiliLoginPage as bp

# 获取当前文件所在目录
root = os.path.dirname(os.path.abspath(__file__))


@allure.feature("模块：b站登录")
class TestChannel(bp):

    @pytest.mark.P1
    @allure.story("正向登录测试")
    def test_bilibili_login(self, refresh_web):
        """
        b站登录模块正向测试
        """
        # result_text = bp(refresh_web).webstar()
        # assert result_text != "登录"
        page_title = bp(refresh_web).login_process()
        assert page_title == "登录验证"
