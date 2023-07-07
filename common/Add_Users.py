# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   RanZhi
# FileName:     Add_Users
# Author:      Pengfukun
# Datetime:    2021/5/21 17:19
# Description：
#-----------------------------------------------------------------------------------
from common.Login import Login

from time import sleep

from page.py_ranzhi import RanZhi

from selenium.webdriver.support.select import Select
class Add_Users(Login):

    # def __init__(self):
    #     # 管理员登录
    #     self.login_ranzhi("admin", "123456")
    #

    def add_users(self,username,realname,sex,dept,juse,pwd1,pwd2,email):
        # 输入用户名
        self.send_key("i,account", username)
        # 输入真实姓名
        self.send_key("i,realname", realname)
        # 输入性别
        self.click("i,{}".format(sex))
        # s输入部门
        Select(self.locator_element("i,dept")).select_by_value(dept)
        # self.login.locator2("i,dept","t,option",dept)
        # 输入角色
        Select(self.locator_element("i,role")).select_by_value(juse)
        # self.login.locator2("i,dept", "t,option", juse)
        # 输入密码
        self.send_key("i,password1", pwd1)
        # 确认密码
        self.send_key("i,password2", pwd2)
        # 输入邮箱
        self.send_key("i,email", email)
        # 点击保存
        self.click("i,submit")

if __name__ == '__main__':
    add_users=Add_Users()


