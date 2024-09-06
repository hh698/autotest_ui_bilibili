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

    # 打开 allure 报告
    # 说明：open相当打开一个tomcat服务，并用端口8883进行监听，监听端口不冲突时可以任意设置
    allure_open_command = "allure open -h 127.0.0.1 -p 8883 Outputs/reports/allure_reports/html"
    run_command(allure_open_command)
