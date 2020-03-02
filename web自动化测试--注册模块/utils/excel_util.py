import time

from xlutils.copy import copy
import xlrd


class ExcelUtil:

    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            self.excel_path = r"D:\测试\自动化测试\Web自动化测试\web自动化测试--注册模块\config\casedata.xls"
        else:
            self.excel_path = excel_path
        if index is None:
            self.index = 0
        else:
            self.index = index
        # 获取一个excel工作薄对象
        self.data = xlrd.open_workbook(self.excel_path)
        # 获取第index个excel工作表对象
        self.table = self.data.sheets()[self.index]

    def get_data(self):
        """
        一行数据组成一个list，并将所有行组成的list存入一个list
        :return: 所有行数据list组成的list
        """
        result = []
        rows = self.get_lines()
        if rows is None:
            return None
        else:
            for i in range(rows):
                # 获取第i行的所有数据并存入一个list中
                col = self.table.row_values(i)
                for j in range(len(col)):
                    # 如果检测到float类型则转化为int类型
                    if isinstance(col[j], float):
                        col[j] = int(col[j])
                result.append(col)
            return result

    def get_lines(self):
        # 获取excel的行数
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    def get_col_values(self, row, col):
        """
        获取单元格的数据
        :return:
        """
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    # 写入数据
    def write_value(self, row, value):
        # 打开excel并创建一个excel工作薄对象
        read_value = xlrd.open_workbook(self.excel_path)
        # 复制整个excel工作薄对象
        write_data = copy(read_value)
        # 在第一个excel工作表的第row行第9列写入value
        write_data.get_sheet(0).write(row, 9, value)
        # 将修改后的excel工作薄存储
        write_data.save(self.excel_path)
        time.sleep(1)


if __name__ == "__main__":
    ex = ExcelUtil(excel_path=r"D:\测试\自动化测试\Web自动化测试\selenium3_python3\config\keyword.xls")
    res = ex.get_col_values(2, 3)
    print(res)
    # ex.write_value(11, "")