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
        bp(refresh_web).webstar()
        bp(refresh_web).pass_touclick(username="1277490394", password="1277490394", img_path='image.png',
                                          ID="08272733")
        bp(refresh_web).click_confirm_button()

        assert bp(refresh_web).do_get_title() != "登录"
