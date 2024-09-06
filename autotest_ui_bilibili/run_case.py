import os
import subprocess
import sys
import webbrowser


def run_tests():
    # 运行pytest测试
    # 执行pytest，生成allure的json结果文件
    pytest_cmd = [
        "pytest", "--alluredir", "Outputs/reports/allure_results", "--clean-alluredir"
    ]
    try:
        subprocess.run(pytest_cmd, check=True, stderr=subprocess.PIPE)
        print("测试成功！")
    except subprocess.CalledProcessError as e:
        print("测试失败，错误信息：")
        print(e.stderr.decode('utf-8'))
        return

    # 生成Allure报告
    allure_cmd = [
        "allure", "generate", "Outputs/reports/allure_results", "-o", "Outputs/reports/allure_reports", "--clean"
    ]
    print(allure_cmd)
    try:
        subprocess.run(allure_cmd, check=True)
        print("Allure报告生成成功！")
    except subprocess.CalledProcessError as e:
        print("Allure报告生成失败，错误信息：")
        print(e.stderr.decode('utf-8'))  # 解码stderr输出
        return

    # 打开Allure报告
    report_path = os.path.join("Outputs/reports/allure_reports", "index.html")
    webbrowser.open("file://" + report_path)


if __name__ == "__main__":
    try:
        run_tests()
        print("测试结束！")
    except Exception as e:
        print("测试中断：")
        print(e)
