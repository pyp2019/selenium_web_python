import time

from handle.register_handle import RegisterHandle


class RegisterBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.register_h = RegisterHandle(self.driver)

    # 执行操作
    # def user_base(self, email, name, password, file_name, code=None):
    #     self.register_h.send_user_email(email)
    #     self.register_h.send_user_name(name)
    #     self.register_h.send_user_password(password)
    #     self.register_h.send_user_code(file_name, code)
    #     self.register_h.click_register_button()

    def user_base(self, email, name, password, code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code=code)
        self.register_h.click_register_button()

    def error_base(self, info, user_info):
        try:
            base = self.register_h.get_user_error(info, user_info)
        except:
            return True
        else:
            if base:
                return False
            else:
                return True

    def pass_base(self, info, user_info):
        try:
            base = self.register_h.get_user_error(info, user_info)
        except:
            return False
        else:
            if base:
                return True
            else:
                return False

    def register_function(self, email, nickname, password, code, assertCode, assertText):
        try:
            self.user_base(email, nickname, password, code)
        except:
            return True
        if "error" in assertCode:
            return self.error_base(assertCode, assertText)
        else:
            return self.pass_base(assertCode, assertText)

    def register_success(self, email, name, password, file_name):
        self.user_base(email, name, password, file_name)
        try:
            self.register_h.get_register_text()
        except:
            return False
        else:
            print("注册失败")
            return True

    def email_error(self, email, name, password, file_name):
        """
            邮箱错误
        """
        self.user_base(email, name, password, file_name)
        return self.error_base("email", "邮箱验证不成功")

    def name_error(self, email, name, password, file_name):
        """
            用户名错误
        """
        self.user_base(email, name, password, file_name)
        return self.error_base("name", "用户名验证不成功")

    def password_error(self, email, name, password, file_name):
        """
            密码错误
        """
        self.user_base(email, name, password, file_name)
        return self.error_base("password", "密码验证不成功")

    def code_error(self, email, name, password, code):
        """
            验证码错误
        """
        self.user_base(email, name, password, None, code)
        return self.error_base("code", "验证码验证不成功")