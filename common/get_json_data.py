# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   Python_28
# FileName:     get_json_data
# Author:      Pengfukun
# Datetime:    2021/5/20 14:49
# Description：
#-----------------------------------------------------------------------------------
import json
def get_json_data(path):
    with open(path,encoding="utf8") as j_json:
        return json.load(j_json)
if __name__ == '__main__':
    get_json_data(r"C:\Users\Administrator\PycharmProjects\Python_28\Day_5_20\case_json.json")