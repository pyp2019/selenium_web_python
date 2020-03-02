import time

from PIL import Image

from pages.base_page import BasePage
from utils.ShowapiRequest import ShowapiRequest


class GetCode:
    def __init__(self, driver):
        self.driver = driver

    def get_user_element(self, key):
        """
        定位用户信息，获取element
        :param key: 配置文件的key
        :return: 返回定位的元素的位置element
        """
        find_element = BasePage(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    # 获取图片
    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        # 定位网页上的验证码图片
        code_element = self.get_user_element("code_image")
        # 获取id为getcode_num的图片的所在位置的左上角的坐标
        # coor = code_element.location  # {"x": 123, "y": 456}
        # 获取id为getcode_num的图片的x轴长度
        width = code_element.size['width']
        # 获取id为getcode_num的图片的y轴长度
        height = code_element.size['height']
        # 左坐标
        left_coor = code_element.location["x"]
        # 顶左标
        top_coor = code_element.location["y"]
        # 右坐标
        right_coor = width + left_coor
        # 下坐标
        height_coor = height + top_coor
        # 打开图片
        im = Image.open(file_name)
        # 裁剪图片
        img = im.crop((left_coor, top_coor, right_coor, height_coor))
        # 保存裁剪后的图片
        img.save(file_name)
        time.sleep(5)

    # 解析图片，获取验证码
    def code_online(self, file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/1274-2", "143640", "e2756fc88a784b7e8e9c234258111e5c")
        r.addFilePara("imgFile", file_name)
        res = r.post()
        print(res.text)
        text = res.json()["showapi_res_body"]["texts"][0][:5]
        # print(text)
        time.sleep(2)
        return text