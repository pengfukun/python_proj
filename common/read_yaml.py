# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   Python_28
# FileName:     read_yaml
# Author:      Pengfukun
# Datetime:    2021/5/19 14:31
# Description：
#-----------------------------------------------------------------------------------
import yaml
def read_yaml_data(path):
    with open(path,mode='r',encoding='utf8')as yaml1:
        return yaml.safe_load(yaml1)
if __name__ == '__main__':
    print(read_yaml_data(r"C:\Users\Administrator\PycharmProjects\Python_28\Day_5_20\case_yaml.yaml"))
