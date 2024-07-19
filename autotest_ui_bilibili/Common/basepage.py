from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    # 等待元素可见
    # def wait_elevisible(self, loc, timeout=120, frequency=0.5, doc=""):
    #     """
    #     :param loc:
    #     :param timeout:
    #     :param frequency:
    #     :param doc:
    #     :return:
    #     """
    #     start_time = time.time()
    #     try:
    #         WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
    #     except Exception as e:
    #         logger.logging.exception("等待{}元素可见超时".format(loc))
    #         self.do_save_screenshot(doc)
    #         raise
    #     else:
    #         end_time = time.time()
    #         duration = end_time - start_time
    #         logger.logging.info("等待{}元素可见,耗时{}".format(loc, duration))

    def ele_click(self):
        pass

    def ele_send_keys(self):
        pass

    def ele_clear(self):
        pass

    def ele_get_text(self):
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
