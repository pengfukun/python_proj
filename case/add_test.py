# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   RanZhi
# FileName:     AddUsers
# Author:      Pengfukun
# Datetime:    2021/5/22 9:08
# Description：
#-----------------------------------------------------------------------------------
import unittest
from time import sleep
import time
from parameterized import parameterized
from common.Add_Users import Add_Users
from common.get_json_data import get_json_data
from common.get_log import get_logging
from common.read_ini import ReadIni
class AddUsers(unittest.TestCase):
    case_json=get_json_data(ReadIni().get_jsonpath())
    tt=time.strftime("%Y_%m_%d_%H_%M_%S")
    log_path = ReadIni().get_logpath() + "log{}.log".format(tt)
    @classmethod
    def setUpClass(self):
        self.add = Add_Users("c")
        self.add.login_ranzhi("admin","123456")
        # 进入后台管理
        self.add.click('x,//*[@id="s-menu-superadmin"]/button')
        # 进入框架
        self.add.swtich_to_iframe('x,//*[@id="iframe-superadmin"]')
        # 点击添加人员
        self.add.click('x,//*[@id="shortcutBox"]/div/div[1]/div/a/h3')
    @classmethod
    def tearDownClass(self):
        self.add.sleepandquit()
    # def setUp(self):
    #    pass
    @parameterized.expand(case_json["test_addsuccess"])
    def test_addasuccess(self,username,realname,sex,dept,juse,pwd1,pwd2,email,assertaa,num):
        try:
            self.add.add_users(username,realname,sex,dept,juse,pwd1,pwd2,email)
            sleep(2)
            # 跳转至最后一页
            self.add.send_key("i,_pageID", "1000")
            # 点击goto
            self.add.click("i,goto")
            sleep(1)
            # username1 = self.add.get_text("x,{}".format(assert_))
            # userassert=self.add_.get_text('x,//*[@id="accountLabel"]')
            # self.assertEqual()
            #断言
            username1=self.add.get_text(assertaa)
            self.assertEqual(username,username1,msg="断言失败，第{}条有问题".format(num))
        finally:
            # 点击添加成员
            self.add.click('x,/html/body/div/div/div/div[1]/div/div[2]/a[1]')
    @parameterized.expand(case_json["test_addfail"])
    def test_addfail(self,username,realname,sex,dept,juse,pwd1,pwd2,email,yuqi,assertaa,num):
        #调用添加成员
        self.add.add_users(username,realname,sex,dept,juse,pwd1,pwd2,email)
        #断言错误信息
        try:
            shiji=self.add.get_text(assertaa)
            self.assertIn(yuqi,shiji,msg="第{}有错误".format(num))

        except:
            tt = time.strftime("%Y_%m_%d_%H_%M_%S")
            self.add.get_screenshot(ReadIni().get_screenshotpath() + "screenshot{}.png".format(tt))
            get_logging(self.log_path).error("预期与实际不一致,第{}条有问题".format(num))
            raise AssertionError("预期与实际不一致,第{}条有问题".format(num))





if __name__ == '__main__':
    unittest.main()
