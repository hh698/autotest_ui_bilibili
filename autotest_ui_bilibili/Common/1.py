# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time
#
# # 创建 Chrome 选项
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", False)
#
# # 初始化 WebDriver 实例
# driver = webdriver.Chrome(options=chrome_options, service=Service())
#
# # 打开一个网页
# driver.get("https://www.baidu.com")
#
# # 等待一段时间
#
# time.sleep(3)

import os
import subprocess
import sys
import logging
import threading

import pytest


# def run_tests():
#     pytest.main()
#     print("用例执行成功，json生成完毕！")
#     allure_cmd = "allure generate Outputs/reports/allure_results -o Outputs/reports/allure_reports/html --clean"
#     try:
#         subprocess.run(allure_cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         print("Allure报告生成成功！")
#     except subprocess.CalledProcessError as e:
#         print("Allure报告生成失败，错误信息：")
#         print(e.stderr.decode('utf-8'))  # 解码stderr输出
#         return
#
#     def run_command_in_thread(command):
#         def target():
#             try:
#                 subprocess.run(command, shell=True, check=True)
#                 logging.info(f"Command executed in thread: {command}")
#             except subprocess.CalledProcessError as e:
#                 logging.error(f"Command execution failed in thread: {command}")
#                 logging.error(e.stderr.decode() if e.stderr else "")
#
#         thread = threading.Thread(target=target)
#         thread.start()
#     allure_open_command = "allure open -h 127.0.0.1 -p 8882 Outputs/reports/allure_reports/html"
#     run_command_in_thread(allure_open_command)
#     print("Allure报告已打开！")
#
#     if __name__ == "__main__":
#         try:
#             run_tests()
#             print("测试结束！")
#         except Exception as e:
#             print("测试中断：")
#             print(e)


import logging

# 创建 logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # 设置日志级别

# 创建 handler，输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 创建 formatter 并将其添加到 handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# 将 handler 添加到 logger
logger.addHandler(ch)

# 测试日志
logger.info("This is an info message")
logger.error("This is an error message")