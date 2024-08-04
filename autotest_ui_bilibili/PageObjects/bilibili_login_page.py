from Common.basepage import BasePage
from PageLocators.bilibili_login_page_locator import BilibiliLoginPageLocator as bp


class BilibiliLoginPage(BasePage):
    def login(self):
        self.wait_click_ele(bp.login_button)
        self.wait_click_ele(bp.username_input)
        self.ele_send_keys(bp.login_button)
        self.wait_click_ele(bp.password_input)
        self.ele_send_keys(bp.password_input)
        text_search = self.ele_get_text(bp.login_button)
        return text_search
