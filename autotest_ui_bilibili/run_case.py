import os
import subprocess
import sys
import webbrowser


def run_tests():
    # 运行pytest测试
    # 执行pytest，生成allure的json结果文件
    pytest_cmd = [
        "pytest",
        "--alluredir", "F:\\GitHub\\autotest_ui_bilibili\\autotest_ui_bilibili\\Outputs\\reports\\allure_results"
    ]
    try:
        subprocess.run(pytest_cmd, check=True, stderr=subprocess.PIPE)
        print("测试成功！")
    except subprocess.CalledProcessError as e:
        print("测试失败，错误信息：")
        print(e.stderr.decode())

    # 生成Allure报告
    allure_cmd = [
        "allure", "generate",
        "F:\\GitHub\\autotest_ui_bilibili\\autotest_ui_bilibili\\Outputs\\reports\\allure_results", "--clean-alluredir",
        "-o",
        "F:\\GitHub\\autotest_ui_bilibili\\autotest_ui_bilibili\\Outputs\\reports\\allure_reports"
    ]
    print(allure_cmd)
    subprocess.run(allure_cmd, check=True)

    # 打开Allure报告
    report_path = os.path.join("Outputs", "reports", "allure_report", "testreport.html")
    webbrowser.open("file://" + report_path)


if __name__ == "__main__":
    run_tests()
