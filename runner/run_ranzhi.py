# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   RanZhi
# FileName:     run_ranzhi
# Author:      Pengfukun
# Datetime:    2021/5/21 14:49
# Description：
#-----------------------------------------------------------------------------------
import unittest
from unittestreport import TestRunner
from common.read_ini import ReadIni
import time

from common.send_email import SendEmail


class Runner():
    def run_ranzhi(self):
        #实例化测试条件
        # suit=unittest.TestSuite()
        #获取用例地址
        case_path=ReadIni().get_case_path()
        # 获取测试报告地址
        t=time.strftime("%Y_%m_%d_%H_%M_%S")
        report_path=ReadIni().get_report_path()+"report{}.html".format(t)
        #添加用例到测试套件中
        # 加载用例第一种方法
        # suit.addTests(unittest.TestLoader().discover(case_path,pattern="login_test.py"))
        # 加载用例第二种方法(不实例化testsuit)
        suit=unittest.defaultTestLoader.discover(case_path,pattern="*.py")
        # 加载用例第三种方法，通过类名查找到用例
        # suit=unittest.defaultTestLoader.loadTestsFromTestCase(loginTest)
        # 打印测试 报告
        # 方法一
        run_ran=TestRunner(suit,report_path,report_path,title="然之测试报告",desc="哈哈哈哈哈",templates=2)
        run_ran.run()
        SendEmail().send_email(report_path)
if __name__ == '__main__':
    runm=Runner()
    runm.run_ranzhi()


