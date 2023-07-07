# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   RanZhi
# FileName:     addfile_test
# Author:      Pengfukun
# Datetime:    2021/5/23 17:54
# Description：
#-----------------------------------------------------------------------------------
import unittest
from time import sleep
import time

from common.get_json_data import get_json_data
from common.get_log import get_logging
from common.read_ini import ReadIni
from page.add_file import Add_File
from parameterized import parameterized
class Add_File1(unittest.TestCase):
    case_json=get_json_data(ReadIni().get_jsonpath())
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
        # 点击第一个文档库
        self.addfilebox.click('x,//*[@id="libs"]/div/div[1]/div/a')
    def setUp(self):
        # 点击创建文档
        self.addfilebox.click('x,//*[@id="menuActions"]/a')
    @classmethod
    def tearDownClass(self):
        self.addfilebox.sleepandquit()
    @parameterized.expand(case_json["add_linkfile_success"])
    def test_addfile_success(self,fenlei,user,type,title,content,keywords,abstract,fileBox1,fileBox1title,fileBox2,fileBox2title,shiji,num,*url):
        try:
            self.addfilebox.add_file(fenlei,user,type,title,content,keywords,abstract,fileBox1,fileBox1title,fileBox2,fileBox2title,*url)
            sleep(2)
            # 跳转至最后一页
            self.addfilebox.send_key("i,_pageID", "1000")
            # 点击goto
            self.addfilebox.click("i,goto")
            sleep(1)
            #断言
            shiji1=self.addfilebox.get_text(shiji)
            self.assertEqual(title,shiji1,msg="第{}条有问题".format(num))
            # # 点击添加文档
            # self.addfilebox.click('x,//*[@id="menuActions"]/a')
        except:
            tt = time.strftime("%Y_%m_%d_%H_%M_%S")
            self.addfilebox.get_screenshot(ReadIni().get_screenshotpath() + "screenshot{}.png".format(tt))
            get_logging(self.log_path).error("预期与实际不一致,第{}条有问题".format(num))
            raise AssertionError("预期与实际不一致,第{}条有问题".format(num))

    @parameterized.expand(case_json["add_linkfile_fail"])
    def test_addfile_fail(self, fenlei, user, type, title, content, keywords, abstract, fileBox1,
                                 fileBox1title, fileBox2, fileBox2title, yuqi,shiji, num, *url):
        try:
            self.addfilebox.add_file(fenlei, user, type, title, content, keywords, abstract, fileBox1,
                                     fileBox1title, fileBox2, fileBox2title, *url)
            # 断言
            shiji1 = self.addfilebox.get_text(shiji)
            self.assertEqual(yuqi, shiji1, msg="第{}条有问题".format(num))
            # # 点击添加文档
            # self.addfilebox.click('x,//*[@id="menuActions"]/a')
        except:
            tt = time.strftime("%Y_%m_%d_%H_%M_%S")
            self.addfilebox.get_screenshot(ReadIni().get_screenshotpath() + "screenshot{}.png".format(tt))
            get_logging(self.log_path).error("预期与实际不一致,第{}条有问题".format(num))
            raise AssertionError("预期与实际不一致,第{}条有问题".format(num))
        finally:
            #js滚动条
            js = "arguments[0].scrollIntoView()"
            ele_wntj=self.addfilebox.locator_element('x,//*[@id="ajaxForm"]/table/tbody/tr[11]/td/a')
            self.addfilebox.driver.execute_script(js,ele_wntj)
            #点击返回
            self.addfilebox.click('x,//*[@id="ajaxForm"]/table/tbody/tr[11]/td/a')
            sleep(1)

if __name__ == '__main__':
    unittest.main()

