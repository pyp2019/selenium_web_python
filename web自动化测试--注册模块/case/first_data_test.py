import ddt
import unittest
import time
import os
from selenium import webdriver
from business.register_business import RegisterBusiness
import HTMLTestRunner

from utils.excel_util import ExcelUtil

ex = ExcelUtil()
data = ex.get_data()


@ddt.ddt
class FirstDataTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     option = webdriver.ChromeOptions()
    #     # 无界面使用
    #     option.add_argument('--headless')
    #     # 设置浏览器分辨率（窗口大小
    #     option.add_argument("--window-size=1920,1080")
    #     cls.driver = webdriver.Chrome(chrome_options=option)
    #     cls.driver.get("http://www.5itest.cn/register")
    #     cls.register_b = RegisterBusiness(cls.driver)

    def setUp(self):
        print("开始执行case")
        option = webdriver.ChromeOptions()
        # 无界面使用
        option.add_argument('--headless')
        # 设置浏览器分辨率（窗口大小
        option.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.get("http://www.5itest.cn/register")
        self.register_b = RegisterBusiness(self.driver)
        # self.file_name = r"D:\测试\自动化测试\Web自动化测试\selenium3_python3\image\code.png"

    # @classmethod
    # def tearDownClass(cls):
    #     time.sleep(5)
    #     cls.driver.quit()

    def tearDown(self):
        print("case执行结束")
        time.sleep(2)
        self.driver.quit()
        # for method_name, error in self._outcome.errors:
        #     if error:
        #         # case_name是测试函数名
        #         case_name = self._testMethodName
        #         now_time = time.strftime("%Y%m%d.%H.%M.%S")
        #         self.driver.save_screenshot(r"D:\测试\自动化测试\Web自动化测试\selenium3_python3\image\%s.png" % (case_name + now_time))

    # 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
    # ["email", "nickname", "password", "code", "assertCode", "assertText"]
    # @ddt.data(
    #     ['12', 'Mushishi01', '111111', 'code', 'email_error', '请输入有效的电子邮件地址'],
    #     ['@qq.com', 'Mushishi01', '111111', 'code', 'email_error', '请输入有效的电子邮件地址'],
    #     ['12@qq.com', 'Mushishi01', '111111', 'code', 'email_error', '请输入有效的电子邮件地址'],
    # )
    # @ddt.unpack

    @ddt.data(*data)
    def test_register_case(self, data):
        email, nickname, password, code, assertCode, assertText = data
        register_error = self.register_b.register_function(email, nickname, password, code, assertCode, assertText)
        self.assertFalse(register_error, "此条case执行失败")


if __name__ == "__main__":
    # unittest.main()
    file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/report/" + "first_case1.html"
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDataTest)
    with open(file_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report", description=u"这个是我们第一次测试报告", verbosity=2)
        runner.run(suite)