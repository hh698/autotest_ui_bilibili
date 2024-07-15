from PIL import Image
from selenium import webdriver
import time
from selenium.webdriver import ActionChains  # 鼠标悬停动作链
from selenium.webdriver.common.by import By
import base64
import json
import requests
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://passport.bilibili.com/login")


def webstar():
    # driver.set_window_size(1200, 1000)
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入账号"]').send_keys("15671392055")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入密码"]').send_keys("hfq990921")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '.btn_primary ').click()


def b64_api(username, password, img_path, ID):
    with open(img_path, 'rb') as f:
        b64_data = base64.b64encode(f.read())
    b64 = b64_data.decode()
    data = {"username": username, "password": password, "ID": ID, "b64": b64, "version": "3.1.1"}
    data_json = json.dumps(data)
    result = json.loads(requests.post("http://www.fdyscloud.com.cn/tuling/predict", data=data_json).text)
    return result


def pass_touclick():
    time.sleep(2)
    driver.get_screenshot_as_file('browser.png')
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
    result_json = b64_api(username="1277490394", password="1277490394", img_path=img_path, ID="08272733")
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
def click_confirm_button():
    driver.find_element(By.CSS_SELECTOR, '.geetest_commit_tip').click()


if __name__ == '__main__':
    webstar()
    pass_touclick()
    click_confirm_button()
