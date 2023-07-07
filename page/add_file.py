# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   RanZhi
# FileName:     add_file
# Author:      Pengfukun
# Datetime:    2021/5/22 15:49
# Description：
# -----------------------------------------------------------------------------------
from time import sleep
from selenium.webdriver.support.select import Select
from common.Login import Login
class Add_File(Login):
    def add_filebox(self,filetype,filename,private):
        sleep(1)
        # 点击创建文档库
        self.click('x,//*[@id="createButton"]')
        # 点击文档类型
        # random(self.locator2("i,libType","t,option"))
        Select(self.locator_element("i,libType")).select_by_value(filetype)
        # 输入文件名字
        self.send_key('x,//*[@id="name"]', filename)
        # 授权用户
        self.click('x,//*[@id="users_chosen"]/ul')
        self.click('x,//*[@id="users_chosen"]/div/ul/li[1]')
        # 授权分组
        self.click('x,//*[@id="groups1"]')
        #设为私密
        if private==("true"or "t"):
            self.click('i,private')
        # 点击保存
        self.click('i,submit')
    def add_file(self,fenlei,user,type,title,content,keywords,abstract,fileBox1,fileBox1title,fileBox2,fileBox2title,*url):
        sleep(1)
        # # 点击创建文档
        # self.click('x,//*[@id="menuActions"]/a')
        # 点击所属分类
        Select(self.locator_element('i,module')).select_by_value(fenlei)
        # 授权用户
        self.click('x,//*[@id="users_chosen"]/ul')
        self.click('x,//*[@id="users_chosen"]/div/ul/li[{}]'.format(user))
        # 授权分组
        self.click('i,groups2')
        sleep(2)
        if type == ("url" or "链接"):
            self.add_link(title,keywords,abstract,fileBox1,fileBox1title,fileBox2,fileBox2title,url)
        else:
            self.add_doc(title,content,keywords,abstract,fileBox1,fileBox1title,fileBox2,fileBox2title)
    def add_link(self,title,keywords,abstract,fileBox1,fileBox1title,fileBox2,fileBox2title,url):
        # 点击链接类型
        self.click('i,typeurl')
        #点击标题
        self.send_key('i,title',title)
        #文档url
        self.send_key('i,url',url)
        #关键字
        self.send_key('i,keywords',keywords)
        #摘要
        self.send_key('i,digest',abstract)
        # 附件1
        self.send_key('x,//*[@id="fileBox1"]/tbody/tr/td[1]/div/input', fileBox1)
        # 标题1
        self.send_key('x,//*[@id="fileBox1"]/tbody/tr/td[2]/input', fileBox1title)
        # 附件2
        self.send_key('x,//*[@id="fileBox2"]/tbody/tr/td[1]/div/input', fileBox2)
        # 标题2
        self.send_key('x,//*[@id="fileBox2"]/tbody/tr/td[2]/input', fileBox2title)
        # 点击提交
        self.click('i,submit')
        # 点击返回
        # self.click('x,//*[@id="ajaxForm"]/table/tbody/tr[11]/td/a')

    # 文档类型
    def add_doc(self,title,content,keywords,abstract,fileBox1,fileBox1title,fileBox2,fileBox2title):
        # 点击文档类型
        self.click('i,typetext')
        # 输入标题
        self.send_key('i,title', title)
        # 进入框架ueditor_0
        self.swtich_to_iframe('x,//*[@id="ueditor_0"]')
        # 正文
        self.send_key('x,/html/body', content)
        # 退出框架
        self.driver.switch_to.parent_frame()
        # #滚动条
        # self.driver.execute_script("window.scrollBy(0,100)")
        # sleep(1)
        # 关键字
        self.send_key('i,keywords', keywords)
        # 文档摘要
        self.send_key('i,digest', abstract)
        # 附件1
        self.send_key('x,//*[@id="fileBox1"]/tbody/tr/td[1]/div/input', fileBox1)
        # 标题1
        self.send_key('x,//*[@id="fileBox1"]/tbody/tr/td[2]/input', fileBox1title)
        # 附件2
        self.send_key('x,//*[@id="fileBox2"]/tbody/tr/td[1]/div/input', fileBox2)
        # 标题2
        self.send_key('x,//*[@id="fileBox2"]/tbody/tr/td[2]/input', fileBox2title)
        # 点击提交
        self.click('i,submit')
        # 点击返回
        # self.click('x,//*[@id="ajaxForm"]/table/tbody/tr[11]/td/a')


if __name__ == '__main__':
    addfile = Add_File("c")
    addfile.add_filebox('custom','wode wendang 1','a')
    addfile.add_file('0',1,"url","静夜思","窗前明月光","月光","李白",r"c:\login.xlsx","诗歌",r"c:\login.xlsx","诗歌2",r"c:\asd")
