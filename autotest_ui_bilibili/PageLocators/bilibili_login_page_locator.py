from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml


# 封装首页的登录元素
class BilibiliLoginPageLocator:
    # driver = webdriver.Chrome()
    # # driver.get("https://www.bilibili.com/")
    # driver.get("https://passport.bilibili.com/login")
    # driver.maximize_window()

    # 点击唤起首页右上角的登录按钮
    # login_button = (By.CSS_SELECTOR, '.header-login-entry>span')
    # username_input = (By.CSS_SELECTOR, 'input[placeholder="请输入账号"]')
    # password_input = (By.CSS_SELECTOR, 'input[placeholder="请输入密码"]')
    login_button = (By.CSS_SELECTOR, '.form__item>input')
    username_input = (By.CSS_SELECTOR, '.form__item>input[placeholder="请输入账号"]')
    password_input = (By.CSS_SELECTOR, '.form__item>input[placeholder="请输入密码"]')
    # 确定登录
    # confirmLogin_button = (By.CSS_SELECTOR, 'div[class="btn_primary disabled"]')
    confirmLogin_button = (By.CSS_SELECTOR, 'div.btn_primary')

    x = (By.CLASS_NAME, 'btn_primary disabled')
    # 验证码确定按钮
    confirmCode_button = (By.CSS_SELECTOR, '.geetest_commit_tip')

    phone_num = '15671392055'
    phone_password = 'hfq990921'
