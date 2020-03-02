import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_ini import ReadIni


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    # 读取配置文件
    def get_local_config(self, local_config):
        """
        读取配置文件
        :param local_config: 配置文件的key
        :return: 返回值的list
        """
        read_ini = ReadIni()
        ini = read_ini.get_value_tuple(local_config)
        return ini

    # 获取element信息
    def get_element(self, local_config, element=None):
        """
        根据配置的value的list获取element信息
        :param local_config: 含有配置的value值的list
        :param element: 定位元素体
        :return: 返回定位元素体element
        """
        ini = self.get_local_config(local_config)
        locator = (ini[0], ini[1])
        try:
            if element is not None:
                return WebDriverWait(self.driver, 10).until(EC.visibility_of(element.find_element(*locator)))
            else:
                return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=locator))
        except TimeoutException:
            # self.driver.quit()
            raise TimeoutException(msg="定位元素失败，定位方式是:{}".format(locator))
        except NoSuchElementException:
            # self.driver.quit()
            raise NoSuchElementException(msg="定位元素失败，定位方式是:{}".format(locator))