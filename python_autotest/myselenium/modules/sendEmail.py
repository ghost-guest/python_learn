#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020年04月07日 
# @Author  : ghost-guest
# @Site    : 
# @File    : sendEmail.py
# @Software: PyCharm
# 说明： 
#! /usr/bin/python3

import smtplib
import baseInfo
import time
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText

def send_Mail(testReport, result):
    f = open(testReport, 'rb')
    # 读取测试报告正文
    mail_body = f.read()
    f.close()
    try:
        smtp = smtplib.SMTP(baseInfo.mail_server, 25)
        sender = baseInfo.mail_sender
        password = baseInfo.mail_password
        receiver = baseInfo.mail_receiver
        smtp.login(sender, password)
        msg = MIMEMultipart()
        text = MIMEText(mail_body, 'html', 'utf-8')
        msg.attach(text)
        msg['Subject'] = Header('[自动化测试结果：'+result+']', 'utf-8')
        msg['From'] = sender
        msg['To'] = ','.join(receiver)
        msg_file = MIMEText(mail_body, 'html', 'utf-8')
        msg_file['Content-Type'] = 'application/octet-stream'
        msg_file['Content-Disposition'] = 'attachment; filename="report.html"'
        msg.attach(msg_file)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        return True
    except smtplib.SMTPException as e:
        print(str(e))
        return False