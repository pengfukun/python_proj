# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   RanZhi
# FileName:     get_path
# Author:      Pengfukun
# Datetime:    2021/5/20 16:58
# Description：
#-----------------------------------------------------------------------------------
import os
def get_pro_path(path):
    #通过斜杠分隔传入的项目路径
    pro_name=path.split("/")[0]
    print(pro_name)
    #获取当前项目的全路径
    path1=os.path.dirname(__file__)
    print(path1)
    befor_name=path1.split(pro_name)[0]
    print(befor_name)
    return os.path.join(befor_name,path)
if __name__ == '__main__':
    print(get_pro_path("config/case_json.json"))