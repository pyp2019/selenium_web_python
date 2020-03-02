from pages.base_page import BasePage


class RegisterPage():
    def __init__(self, driver):
        self.base = BasePage(driver)

    def get_email_element(self):
        return self.base.get_element("user_email")

    def get_email_error_element(self):
        return self.base.get_element("user_email_error")

    def get_name_element(self):
        return self.base.get_element("user_nickname")

    def get_name_error_element(self):
        return self.base.get_element("user_nickname_error")

    def get_password_element(self):
        return self.base.get_element("user_password")

    def get_password_error_element(self):
        return self.base.get_element("user_password_error")

    def get_code_element(self):
        return self.base.get_element("code_text")

    def get_code_error_element(self):
        return self.base.get_element("code_text_error")

    def get_button_element(self):
        return self.base.get_element("register_button")