import os
import subprocess
import sys
import logging
import threading

import pytest


def run_tests():
    # 运行pytest测试
    # 执行pytest，生成allure的json结果文件
    # pytest_cmd = [
    #     "pytest", "-s", "-v", "--alluredir=Outputs/reports/allure_results", "--clean-alluredir", "--reruns", "2"
    # ]
    # pytest_cmd = "pytest -s -v --alluredir=Outputs/reports/allure_results --clean-alluredir --reruns 2"
    # try:
    #     subprocess.run(pytest_cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     print("测试成功！")
    # except subprocess.CalledProcessError as e:
    #     print("测试失败，错误信息：")
    #     print(e.stderr.decode('utf-8'))
    #     return

    # 不确定subprocess.run无法执行pytest命令，改用pytest.main()
    # 目前的现象是json文件能够正常生成，但是进程在打印之前被堵塞
    pytest.main()
    print("用例执行成功，json生成完毕！")

    # 生成Allure报告
    # 用列表的形式会报错返回非零，不知道原因
    # allure_cmd = [
    #     "allure", "generate", "Outputs/reports/allure_results", "-o", "Outputs/reports/allure_reports", "--clean"
    # ]
    allure_cmd = "allure generate Outputs/reports/allure_results -o Outputs/reports/allure_reports/html --clean"
    try:
        subprocess.run(allure_cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Allure报告生成成功！")
    except subprocess.CalledProcessError as e:
        print("Allure报告生成失败，错误信息：")
        print(e.stderr.decode('utf-8'))  # 解码stderr输出
        return

    # 打开Allure报告
    def run_command_in_thread(command):
        def target():
            try:
                subprocess.run(command, shell=True, check=True)
                logging.info(f"Command executed in thread: {command}")
            except subprocess.CalledProcessError as e:
                logging.error(f"Command execution failed in thread: {command}")
                logging.error(e.stderr.decode() if e.stderr else "")

        thread = threading.Thread(target=target)
        thread.start()
    allure_open_command = "allure open -h 127.0.0.1 -p 8883 Outputs/reports/allure_reports/html"
    run_command_in_thread(allure_open_command)
    print("Allure报告已打开！")
    # 没有加入tomcat进行监听，无法正确打开，目前只能用subprocess.run
    # report_path = os.path.join("Outputs/reports/allure_reports/html", "index.html")
    # webbrowser.open("file://" + report_path)


if __name__ == "__main__":
    try:
        run_tests()
        print("测试结束！")
    except Exception as e:
        print("测试中断：")
        print(e)
