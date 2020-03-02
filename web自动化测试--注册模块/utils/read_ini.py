import configparser


class ReadIni():
    def __init__(self, file_name=None, node=None):
        if file_name == None:
            file_name = r"D:\测试\自动化测试\Web自动化测试\web自动化测试--注册模块\config\LocalElement.ini"
        if node == None:
            self.node = "RegisterElement"
        else:
            self.node = node
        self.data = self.load_ini(file_name)

    # 加载文件
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8-sig")
        return cf

    # 获取key的value
    def get_value(self, key):
        return self.data.get(self.node, key)

    # 拆分>字符两端的字符串并返回list
    def get_value_tuple(self, key):
        data = self.get_value(key)
        data_info = data.split(">")
        return data_info

