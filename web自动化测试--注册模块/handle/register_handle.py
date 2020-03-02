import time

from pages.register_page import RegisterPage
from utils.get_code import GetCode


class RegisterHandle():
    def __init__(self, driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)

    # 输入邮箱
    def send_user_email(self, email):
        element = self.register_p.get_email_element()
        element.clear()
        element.send_keys(email)

    # 输入用户名
    def send_user_name(self, name):
        element = self.register_p.get_name_element()
        element.clear()
        element.send_keys(name)

    # 输入密码
    def send_user_password(self, password):
        element = self.register_p.get_password_element()
        element.clear()
        element.send_keys(password)

    # 输入验证码
    def send_user_code(self, file_name=None, code=None):
        if code:
            pass
        else:
            get_code_text = GetCode(self.driver)
            code = get_code_text.code_online(file_name)
            time.sleep(5)
        element = self.register_p.get_code_element()
        element.clear()
        element.send_keys(code)

    # 点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

    # 获取文字信息
    def get_user_error(self, info, user_info):
        print(user_info)
        if info == "email_error":
            text = self.register_p.get_email_error_element().text
        elif info == "username_error":
            text = self.register_p.get_name_error_element().text
        elif info == "password_error":
            text = self.register_p.get_password_error_element().text
        else:
            text = self.register_p.get_code_error_element().text
        print(text)
        return text == user_info

    # 获取注册按钮文字
    def get_register_text(self):
        self.register_p.get_button_element().text