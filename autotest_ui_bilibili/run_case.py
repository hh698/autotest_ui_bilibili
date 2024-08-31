import subprocess
import sys


def run_tests():
    # 运行pytest测试
    pytest_command = ['pytest']
    result = subprocess.run(pytest_command, text=True, capture_output=True)
    # 检查测试是否通过
    if result.returncode != 0:
        print("Tests failed:")
        print(result.stdout)
        print("Error:", result.stderr)
        sys.exit(result.returncode)
    # 生成Allure报告并打开
    generate_report_command = ['allure', 'generate', 'Outputs/reports/allure-results', '-o',
                               'Outputs/reports/allure-report', '--clean']

    subprocess.run(generate_report_command, check=True)
    open_report_command = ['allure', 'open', 'Outputs/reports/allure-report']
    subprocess.run(open_report_command, check=True)


if __name__ == "__main__":
    run_tests()
