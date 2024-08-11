from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common.basepage import BasePage
from PageLocators.bilibili_login_page_locator import BilibiliLoginPageLocator as bpl
from PageObjects.read_loginyaml import ReadLoginYaml

from PIL import Image
from selenium import webdriver
import time
from selenium.webdriver import ActionChains  # 鼠标悬停动作链
import base64
import json
import requests

# class BilibiliLoginPage(BasePage):
#     def login(self):
#         self.wait_click_ele(bpl.login_button)
#         self.wait_click_ele(bpl.username_input)
#         self.ele_send_keys(bpl.username_input)
#         self.wait_click_ele(bpl.password_input)
#         self.ele_send_keys(bpl.password_input)
#         self.wait_click_ele(bpl.confirmLogin_button)
#         text_search = self.ele_get_text(bpl.login_button)
#         return text_search

driver = webdriver.Chrome()
driver.get("https://passport.bilibili.com/login")
driver.maximize_window()
driver.implicitly_wait(10)


class BilibiliLoginPage(BasePage, ReadLoginYaml):
    def webstar(self):
        # self.wait_click_ele(bpl.login_button)

        phone_number = self.get_phone_number()
        self.ele_send_keys(bpl.username_input, phone_number)
        phone_password = self.get_phone_password()
        self.ele_send_keys(bpl.password_input, phone_password)
        self.wait_click_ele(bpl.confirmLogin_button)

    def b64_api(self, username, password, img_path, ID):
        with open(img_path, 'rb') as f:
            b64_data = base64.b64encode(f.read())
        b64 = b64_data.decode()
        data = {"username": username, "password": password, "ID": ID, "b64": b64, "version": "3.1.1"}
        data_json = json.dumps(data)
        result = json.loads(requests.post("http://www.fdyscloud.com.cn/tuling/predict", data=data_json).text)
        return result

    def pass_touclick(self, username, password, img_path, ID):
        # self.driver.implicitly_wait(10)
        time.sleep(2)
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.presence_of_all_elements_located)

        self.driver.get_screenshot_as_file('browser.png')
        img = Image.open('browser.png')
        width = img.size[0]
        height = img.size[1]
        # 此处求横向与纵向的拉伸率
        # width_stretch_rate = 1200 / int(width)
        # height_stretch_rate = 1000 / int(height)
        # cropped_image = img.crop((862, 470, 1473, 1171))
        cropped_image = img.crop((790, 263, 1114, 680))  # 左、上、右、下
        image_name = 'image.png'
        cropped_image.save(image_name)
        # 调用图灵识别API完成验证码识别
        img_path = image_name
        # result_json = b64_api(username="1277490394", password="1277490394", img_path=img_path, ID="08272733")
        result_json = self.b64_api(username=username, password=password, img_path=img_path, ID=ID)
        # 此处id为模型id
        print(result_json)
        result_data = result_json['data']

        try:
            for i in range(len(result_data)):
                result_order = result_data[f'顺序{i + 1}']
                print(result_order['X坐标值'], result_order['Y坐标值'])
                x_coord = int((int(result_order['X坐标值']) + 790))
                y_coord = int((int(result_order['Y坐标值']) + 260))
                print(x_coord, y_coord)
                ActionChains(driver).move_by_offset(x_coord, y_coord).click().perform()
                ActionChains(driver).move_by_offset(-x_coord, -y_coord).perform()
                time.sleep(2)
        except Exception as e:
            print(e)

        # 点击完成验证码识别

    def click_confirm_button(self):
        self.wait_click_ele(bpl.confirmCode_button)


if __name__ == '__main__':
    bilibili_login_page = BilibiliLoginPage(driver)  # 实例化类
    bilibili_login_page.webstar()
    bilibili_login_page.pass_touclick(username="1277490394", password="1277490394", img_path='image.png', ID="08272733")
    bilibili_login_page.click_confirm_button()
# 下周研究下取出调试之后的代码
# 返回值断言
