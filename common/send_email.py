# -*- coding:utf8 -*- #
#-----------------------------------------------------------------------------------
# ProjectName:   RanZhi
# FileName:     send_email
# Author:      Pengfukun
# Datetime:    2021/5/21 16:20
# Description：
#-----------------------------------------------------------------------------------
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail:
    def send_email(self,report_path):
        try:
            smtp="smtp.163.com"#配置服务器
            port="25"#配置端口
            sender="18113638183@163.com"
            pwd="NBNKIKIQYFTLVZTR"
            receiver="982592212@qq.com;minghong@ronghuanet.com"
            #创建邮件对象，用来设置发送邮件信息
            msg=MIMEMultipart()
            msg["from"]=sender
            msg["to"]=receiver
            msg["subject"]="然之测试报告"
            #读取报告内容
            with open(report_path,mode="rb") as report:
                body=report.read().decode(encoding="utf8")
            #写正文
            mime_text=MIMEText(body,"html","utf8")
            msg.attach(mime_text)

            #添加附件
            att=MIMEText(body,"html","utf8")
            att["Content-Type"]='appliction/octet-strem'#表示可以添加附件
            att["Conten-Disposition"]="attachment:filename=%s" % report_path
            msg .attach(att)
            #发送邮件
            smtp1=smtplib.SMTP()
            smtp1.connect(smtp,port)
            smtp1.login(sender,pwd)
            smtp1.sendmail(sender,receiver.split(";"),msg.as_string())
            print("邮件发送成功")

        except:
            print("邮件发送失败")
if __name__ == '__main__':
    num1=0b1001
    print(bin(num1>>4))

