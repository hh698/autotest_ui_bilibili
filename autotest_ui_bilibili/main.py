# 简单版
# -*- coding: utf-8 -*-
# import os
# import pytest
#
# if __name__ == '__main__':
#     pytest.main()
#     os.system("allure generate Outputs/reports/allure_results -o Outputs/reports/allure_reports/html --clean")
#     # 说明：open相当打开一个tomcat服务，并用端口8883进行监听，监听端口不冲突时可以任意设置
#     os.system("allure open -h 127.0.0.1 -p 8883 Outputs/reports/allure_reports/html")

# 优化版
import subprocess
import logging
import os
import threading

import pytest

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"Command executed successfully: {command}")
        logging.info(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        logging.error(f"Command execution failed: {command}")
        logging.error(e.stderr.decode())


def start_allure_open_in_thread(command):
    thread = threading.Thread(target=run_command, args=(command,))
    thread.start()
    return thread


# def run_command_in_thread(command):
#     def target():
#         try:
#             subprocess.run(command, shell=True, check=True)
#             logging.info(f"Command executed in thread: {command}")
#         except subprocess.CalledProcessError as e:
#             logging.error(f"Command execution failed in thread: {command}")
#             logging.error(e.stderr.decode() if e.stderr else "")
#
#     thread = threading.Thread(target=target)
#     thread.start()


if __name__ == '__main__':
    # 运行 pytest
    pytest.main()
    # pytest.main(["-s", "-v", "--alluredir=Outputs/reports/allure_results", "--clean-alluredir"])

    # 方法一：打开的报告直接在默认浏览器中查看
    # 启动 allure 服务
    # allure_serve_command = "allure serve Outputs/reports/allure_reports/html"
    # run_command(allure_serve_command)

    # 方法二：从结果生成报告（index.html格式，方便随时打开），打开报告，共两步。
    # 生成 allure 报告
    allure_generate_command = "allure generate Outputs/reports/allure_results -o Outputs/reports/allure_reports/html --clean"
    run_command(allure_generate_command)
    print("allure generate finished")

    # 打开 allure 报告
    """
    说明：
    1.open相当打开一个tomcat服务，并用端口8883进行监听，监听端口不冲突时可以任意设置
    2.使用 subprocess.run() 调用 allure open 时，这个命令会启动服务器并阻塞在那里，等待用户输入或关闭。
    由于这个命令没有立即退出，subprocess.run() 也会保持等待状态，因此不会执行到 print("allure open finished") 这一行。
    """
    allure_open_command = "allure open -h 127.0.0.1 -p 8883 Outputs/reports/allure_reports/html"
    start_allure_open_in_thread(allure_open_command)
    # print("allure被一个单独的进程打开")
    # print("继续执行其他任务...")

    print("allure open finished")
