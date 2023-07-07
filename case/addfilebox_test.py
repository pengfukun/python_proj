# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   RanZhi
# FileName:     add_filebox_test
# Author:      Pengfukun
# Datetime:    2021/5/23 15:04
# Description：
#-----------------------------------------------------------------------------------
import unittest
from time import sleep
import time
from parameterized import parameterized
from common.get_json_data import get_json_data
from common.get_log import get_logging
from common.read_ini import ReadIni
from page.add_file import Add_File
class Add_FileBox_test(unittest.TestCase):
    case_addboxs=get_json_data(ReadIni().get_jsonpath())
    tt = time.strftime("%Y_%m_%d_%H_%M_%S")
    log_path = ReadIni().get_logpath() + "log{}.log".format(tt)
    @classmethod
    def setUpClass(self):
        self.addfilebox = Add_File("c")
        self.addfilebox.login_ranzhi("admin", "123456")
        # 点击文档
        self.addfilebox.click('x,//*[@id="s-menu-4"]/button')
        # 进入框架
        self.addfilebox.swtich_to_iframe("i,iframe-4")
        # self.addfilebox.add_filebox()
    @classmethod
    def tearDownClass(self):
        self.addfilebox.sleepandquit()

    @parameterized.expand(case_addboxs["test_addfile_success"])
    def test_add_success(self,filetype,filename,private,shiji,num):
        try:
            self.addfilebox.add_filebox(filetype,filename,private)
            sleep(2)
            filename1=self.addfilebox.get_text(shiji)
            self.assertEqual(filename,filename1,msg="第{}条有错".format(num))
        except:
            tt = time.strftime("%Y_%m_%d_%H_%M_%S")
            self.addfilebox.get_screenshot(ReadIni().get_screenshotpath() + "screenshot{}.png".format(tt))
            get_logging(self.log_path).error("预期与实际不一致,第{}条有问题".format(num))
            raise AssertionError("预期与实际不一致,第{}条有问题".format(num))
        finally:
            #点击首页
            self.addfilebox.click('x,//*[@id="mainNavbar"]/ul/li[1]/a')

    @parameterized.expand(case_addboxs["test_addfile_fail"])
    def test_add_fail(self,filetype,filename,private,shiji,yuqi,num):
        try:
            self.addfilebox.add_filebox(filetype,filename,private)
            sleep(2)
            filename1=self.addfilebox.get_text(shiji)
            self.assertEqual(yuqi,filename1,msg="第{}条有错".format(num))
        except:
            tt = time.strftime("%Y_%m_%d_%H_%M_%S")
            self.addfilebox.get_screenshot(ReadIni().get_screenshotpath() + "screenshot{}.png".format(tt))
            get_logging(self.log_path).error("预期与实际不一致,第{}条有问题".format(num))
            raise AssertionError("预期与实际不一致,第{}条有问题".format(num))
        finally:
            self.addfilebox.click('x,//*[@id="ajaxModal"]/div[2]/div/div[1]/button')
            #点击首页
            self.addfilebox.click('x,//*[@id="mainNavbar"]/ul/li[1]/a')


if __name__ == '__main__':
    unittest.main()
