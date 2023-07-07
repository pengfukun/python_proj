# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   Python_28
# FileName:     read_excel
# Author:      Pengfukun
# Datetime:    2021/5/19 17:20
# Description：
#-----------------------------------------------------------------------------------
import openpyxl

def get_excel_data(path,sheet_name):
    excel_file=openpyxl.load_workbook(path)
    get_sheet=excel_file[sheet_name]
    list_all=[]
    for hang in get_sheet:
        list1=[]
        for i in hang:
            list1.append(i.value)
        list_all.append(list1)
    return list_all[1:]


