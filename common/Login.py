# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   Python_28
# FileName:     Login
# Author:      Pengfukun
# Datetime:    2021/5/19 11:39
# Description：
#-----------------------------------------------------------------------------------
from common.base_pfk import Base
from common.read_ini import ReadIni
from common.read_yaml import read_yaml_data


class Login(Base):
    data=read_yaml_data(ReadIni().get_elepath())
    def login_ranzhi(self,adname,adpwd):

        # 输入账户密码
        self.send_key(self.data["Login"]["USERNAME"], adname)
        self.send_key(self.data["Login"]["PWD"], adpwd)
        # 点击登录
        self.click(self.data["Login"]["BUTTON"])