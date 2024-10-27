import yaml

# file_path = '../PageLocators/login.yaml'
file_path = 'F:\\GitHub\\autotest_ui_bilibili\\autotest_ui_bilibili\\PageLocators\\login.yaml'


class ReadLoginYaml:
    def __init__(self):
        self.config = None
        self.phone_number = ''
        self.phone_password = ''

    def read_yaml(self, file_path):
        """读取YAML文件"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.config = yaml.safe_load(file)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except yaml.YAMLError:
            print(f"Error parsing YAML file: {file_path}")

    def get_phone_number(self):
        # 读取YAML配置文件
        self.read_yaml(file_path)
        # 从配置文件中获取账号
        self.phone_number = self.config.get('phone_number', '') if self.config else ''
        """获取账号"""
        return self.phone_number

    def get_phone_password(self):
        # 读取YAML配置文件
        self.read_yaml(file_path)
        # 从配置文件中获取密码
        self.phone_password = self.config.get('phone_password', '') if self.config else ''
        """获取账号密码"""
        return self.phone_password

    def get_phone_number_2(self):
        # 读取YAML配置文件
        self.read_yaml(file_path)
        # 从配置文件中获取账号
        self.phone_number = self.config.get('phone_number_2', '') if self.config else ''
        """获取账号"""
        return self.phone_number

    def get_phone_password_2(self):
        # 读取YAML配置文件
        self.read_yaml(file_path)
        # 从配置文件中获取密码
        self.phone_password = self.config.get('phone_password_2', '') if self.config else ''
        """获取账号密码"""
        return self.phone_password

    def get_phone_number_3(self):
        # 读取YAML配置文件
        self.read_yaml(file_path)
        # 从配置文件中获取账号
        self.phone_number = self.config.get('phone_number_3', '') if self.config else ''
        """获取账号"""
        return self.phone_number

    def get_phone_password_3(self):
        # 读取YAML配置文件
        self.read_yaml(file_path)
        # 从配置文件中获取密码
        self.phone_password = self.config.get('phone_password_3', '') if self.config else ''
        """获取账号密码"""
        return self.phone_password

    def get_phone_number_4(self):
        # 读取YAML配置文件
        self.read_yaml(file_path)
        # 从配置文件中获取账号
        self.phone_number = self.config.get('phone_number_4', '') if self.config else ''
        """获取账号"""
        return self.phone_number

    def get_phone_password_4(self):
        # 读取YAML配置文件
        self.read_yaml(file_path)
        # 从配置文件中获取密码
        self.phone_password = self.config.get('phone_password_4', '') if self.config else ''
        """获取账号密码"""
        return self.phone_password


if __name__ == '__main__':
    # # 获取当前文件的目录路径
    # current_dir = os.path.dirname(__file__)
    # # 构建配置文件的路径
    # config_file_path = os.path.join(os.path.dirname(current_dir), 'config', 'login_config.yaml')

    file_path = '../PageLocators/login.yaml'
    read = ReadLoginYaml()  # 实例化YourClass，并传入YAML文件路径
    phone_number = read.get_phone_number_2()
    phone_password = read.get_phone_password_2()
    print(phone_number)
    print(phone_password)
