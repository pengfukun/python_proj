# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   Python_28
# FileName:     Test_fun
# Author:      Pengfukun
# Datetime:    2021/5/19 11:47
# Description：
#-----------------------------------------------------------------------------------
from page.py_ranzhi import RanZhi


class Test:
    def test_diao(self):
        add=RanZhi("c")
        add.login_ranzhi("admin","123456")
        name = ["王驰", "古董"]
        add.addmore("admin", "123456", name, 6, 2, "123456", "123456")
if __name__ == '__main__':
    # test=Test()
    # test.test_diao()
    for i in range(10):
        print(i)
