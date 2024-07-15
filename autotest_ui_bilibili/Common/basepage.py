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

