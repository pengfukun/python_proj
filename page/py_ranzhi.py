# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   Python_28
# FileName:     py_ranzhi
# Author:      Pengfukun
# Datetime:    2021/5/17 17:19
# Description：
# -----------------------------------------------------------------------------------
from time import sleep
import random
import string
from common.Login import Login
class RanZhi(Login):
    def addmore(self, realname, username_len, addnum, upwd1, upwd2):
        self.login_ranzhi("admin", "123456")

        username = set()
        sex = ["genderm", "genderf"]
        # 点击后台管理
        self.click('x,//*[@id="s-menu-superadmin"]/button')
        # 进入iframe框架
        self.swtich_to_iframe('x,//*[@id="iframe-superadmin"]')
        self.click('x,//*[@id="shortcutBox"]/div/div[1]/div/a/h3')

        while username.__len__() + 1 <= addnum:
            if username.__len__() <= addnum:
                username.add("".join(random.sample(string.ascii_letters, username_len)))
        try:
            for j in range(addnum):
                # 输入用户名
                username1 = username.pop()
                self.send_key('i,account', username1)
                # 输入真是姓名
                self.send_key('i,realname', realname[j])
                # 选择性别
                self.click('i,{}'.format(random.choice(sex)))
                # 二次定位
                self.locator2('i,dept', "t,option")
                self.locator2('i,role', "t,option")
                # 设置密码和邮箱
                self.send_key('i,password1', upwd1)
                self.send_key('i,password2', upwd2)
                self.send_key('i,email', username1 + "@qq.com")
                # 点击保存
                self.click('i,submit')
                sleep(2)
                # 输入100页
                self.send_key('i,_pageID', 1000)
                # 点击goto
                self.click('i,goto')
                # 断言
                un = self.locator_element(
                    'css,body > div > div > div > div.col-md-10 > div > div > table > tbody > tr:last-child > td:nth-child(3)').text
                print(un)
                if un == username1:
                    print("断言成功")
                else:
                    print("断言失败")
                    print(un)
                    # 点击添加成员
                self.click('x,/html/body/div/div/div/div[1]/div/div[2]/a[1]')

        finally:
            self.sleepandquit()

if __name__ == '__main__':
    ranzhi = RanZhi("c")
    # ranzhi.addmore()
    name = ["王驰", "古董"]
    ranzhi.addmore( name, 6, 2, "123456", "123456")
