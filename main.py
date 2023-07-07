# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   RanZhi
# FileName:     main
# Author:      Pengfukun
# Datetime:    2021/5/21 16:59
# Description：
#-----------------------------------------------------------------------------------
from runner.run_ranzhi import Runner


class Run:
    def run_ranzhi(self):
        run=Runner()
        run.run_ranzhi()
if __name__ == '__main__':
    Run().run_ranzhi()