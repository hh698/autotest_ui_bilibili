from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from PageLocators.bilibili_login_page_locator import BilibiliLoginPageLocator


class BasePage(BilibiliLoginPageLocator):
    def __init__(self, driver):
        self.driver = driver
    #     self.timeout = 20
    #     self.wait = WebDriverWait(self.driver, self.timeout)

    # 等待元素可见
    def wait_elevisible(self, loc, timeout=120, frequency=0.5, doc=""):
        """
        :param loc:
        :param timeout:
        :param frequency:
        :param doc:
        :return:
        """
        start_time = time.time()
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            # logger.logging.exception("等待{}元素可见超时".format(loc))
            self.do_save_screenshot(doc)
            raise
        else:
            end_time = time.time()
            duration = end_time - start_time
            # logger.logging.info("等待{}元素可见,耗时{}".format(loc, duration))

    # 找到元素
    # def get_element(self, locator):
    #     ele = self.driver.find_element(*locator)

    # 等待元素出现并点击
    def wait_click_ele(self, locator):
        try:
            ele = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator))
            ele.click()
        except TimeoutException:
            raise TimeoutException("元素未找到")

    def ele_send_keys(self, locator, value):
        ele = self.driver.find_element(*locator)
        time.sleep(0.5)
        ele.send_keys(value)

    def ele_get_text(self, locator):
        ele = self.driver.find_element(*locator)
        text = ele.text
        return text

    def ele_clear(self):
        pass

    def ele_get_attribute(self):
        pass

    def do_save_screenshot(self):
        pass

    def do_get_title(self):
        pass

    def do_get_url(self):
        pass

    def do_get_window_size(self):
        pass

    def do_get_window_handles(self):
        pass

    def do_get_window_position(self):
        pass

    def do_get_window_maximize(self):
        pass

    def do_get_window_minimize(self):
        pass

    def do_get_alert_text(self):
        pass

    def do_get_alert(self):
        pass

    def do_get_alert_accept(self):
        pass
