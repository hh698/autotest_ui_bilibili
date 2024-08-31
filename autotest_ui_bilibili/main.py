import os
import pytest

if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_login.py"])
    os.system("allure generate ./report/ -o ./report/html --clean")
