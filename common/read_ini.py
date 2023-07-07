# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   RanZhi
# FileName:     read_ini
# Author:      Pengfukun
# Datetime:    2021/5/20 17:46
# Description：
#-----------------------------------------------------------------------------------
import configparser

from common.get_path import get_pro_path
import os

class ReadIni:
    def __init__(self):
        #实例化对象
        self.config=configparser.ConfigParser()
        #获取项目路径
        self.befor_path=get_pro_path("RanZhi")
        #获取ini文件路径
        self.config.read(self.befor_path+r"\config/filepath_ini.ini")
    def get_exclepath(self):
        #获取excel路径
        path=self.config.get("path","excel_path")
        return os.path.join(self.befor_path,path)
    def get_jsonpath(self):
        path=self.config.get("path","json_path")
        return os.path.join(self.befor_path,path)
    def get_yamlpath(self):
        path=self.config.get("path","case_yaml_path")
        return os.path.join(self.befor_path,path)
    def get_elepath(self):
        path=self.config.get("path","ele_path")
        return os.path.join(self.befor_path,path)
    def get_screenshotpath(self):
        path=self.config.get("path","screenshot_path")
        return os.path.join(self.befor_path,path)
    def get_logpath(self):
        path=self.config.get("path","log_path")
        return os.path.join(self.befor_path,path)
    def get_report_path(self):
        path=self.config.get("path","report_path")
        return os.path.join(self.befor_path,path)
    def get_case_path(self):
        path=self.config.get("path","case_path")
        return os.path.join(self.befor_path,path)
if __name__ == '__main__':
    rea=ReadIni()
    print(rea.get_exclepath())
    print(rea.get_jsonpath())
    print(rea.get_yamlpath())
    print(rea.get_elepath())
    print(rea.get_logpath())
    print(rea.get_case_path())
    print(rea.get_report_path())

