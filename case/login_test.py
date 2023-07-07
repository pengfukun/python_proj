# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   Python_28
# FileName:     login_test
# Author:      Pengfukun
# Datetime:    2021/5/19 16:11
# Description：
#-----------------------------------------------------------------------------------
import unittest
from time import sleep
from common.Login import Login
from common.get_json_data import get_json_data
from common.get_log import get_logging
from common.read_excel import get_excel_data
from common.read_ini import ReadIni
from common.read_yaml import read_yaml_data
from parameterized import parameterized
import time
class loginTest(unittest.TestCase):
    data_success=get_excel_data(ReadIni().get_exclepath(),"login_success")
    data_fail=get_excel_data(ReadIni().get_exclepath(),"login_fail")
    case_yaml=read_yaml_data(ReadIni().get_yamlpath())
    case_json=get_json_data(ReadIni().get_jsonpath())
    tt = time.strftime("%Y_%m_%d_%H_%M_%S")
    log_path=ReadIni().get_logpath()+"log{}.log".format(tt)
    @classmethod
    def setUpClass(self):
        self.login = Login("c")
    @classmethod
    def tearDownClass(self):
        self.login.sleepandquit()


    # @parameterized.expand(case_yaml["test_success"])
    @parameterized.expand(case_json["test_success"])
    # @unittest.skip
    def test_success(self,user,pwd,realname,shiji,xuhao):
        try:
            self.login.login_ranzhi(user,pwd)
            self.r_realname=self.login.get_text(shiji)
            self.assertEqual(realname,self.r_realname)
        except:
            self.login.get_screenshot(ReadIni().get_screenshotpath()+"screenshot{}.png".format(self.tt))
            get_logging(self.log_path).error("预期与实际不一致,第{}条有问题".format(xuhao))
            raise AssertionError("预期与实际不一致,第{}条有问题".format(xuhao))
        finally:
            self.login.click('p,签退')
    # @parameterized.expand(data_fail)
    # @parameterized.expand(case_yaml["test_fail"])
    @parameterized.expand(case_json["test_fail"])
    def test_fail(self,user,pwd,shiji,yuqi,xuhao):
        try:
            self.login.login_ranzhi(user,pwd)
            sleep(2)
            self.text=self.login.get_text(shiji)
            self.assertEqual(yuqi,self.text,msg="预期与实际不一致")
        except:
            tt = time.strftime("%Y_%m_%d_%H_%M_%S")
            self.login.get_screenshot(ReadIni().get_screenshotpath() + "screenshot{}.png".format(tt))
            get_logging(self.log_path).error("预期与实际不一致,第{}条有问题".format(xuhao))
            raise AssertionError("预期与实际不一致,第{}条有问题".format(xuhao))
        finally:
            self.login.click('x,/html/body/div[2]/div/div/div[2]/button')

if __name__ == '__main__':
    unittest.main()