import subprocess
import os
import sys


def main():
    # 1. 运行 pytest，生成 allure-results
    print("Running tests...")
    result = subprocess.run([
        sys.executable, "-m", "pytest",
        "testcases/",
        "--alluredir=./allure-results",
        "--clean-alluredir"
    ])
    if result.returncode != 0:
        print("Tests failed. Check the output.")
        # 即使有失败，仍然尝试生成报告（可选）

    # 2. 调 allure 生成报告并打开
    print("Generating and opening Allure report...")

    # 方法：使用 shell=True，并传递完整环境变量
    try:
        subprocess.run("allure serve ./allure-results", shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Failed to run allure command. Make sure Allure is installed and in PATH.")
        print("You can manually run: allure serve ./allure-results")
    except FileNotFoundError:
        print("allure command not found. Please ensure Allure is installed and added to PATH.")
        print("You can manually run: allure serve ./allure-results")


if __name__ == "__main__":
    main()