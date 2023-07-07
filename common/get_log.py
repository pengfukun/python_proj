# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   RanZhi
# FileName:     get_log
# Author:      Pengfukun
# Datetime:    2021/5/21 11:26
# Description：
#-----------------------------------------------------------------------------------
import  logging
def get_logging(log_path):
    #实例化对象
    log=logging.Logger("pro_RanZhi")
    #设置日志格式
    set_format=logging.Formatter("[%(filename)s][%(asctime)s]:%(message)s")
    #打印日志到指定位置
    #实例化对象
    fh=logging.FileHandler(log_path)
    #设置打印格式
    fh.setFormatter(set_format)
    # 打印日志
    log.addHandler(fh)
    return log
