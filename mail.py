# -*- encoding: UTF-8 -*-
'''
@File    :  mail.py
@Time    :  2021/02/28 15:28:17
@Author  :  Kearney
@Contact :  191615342@qq.com
@Desc    :  发送邮件，使用参考README.md
'''
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import os

host_server = 'smtp.qq.com'  # qq邮箱smtp服务器
sender_qq = os.getenv('QQ')  # sender_qq为发件人的qq号码
pwd = os.getenv('PWD')  # pwd为qq邮箱的授权码

receiver = 'lover@love'  # 收件人邮箱
mail_title = 'From Kearney'  # 邮件标题

# 邮件的正文内容
mail_content = '你好，这是使用python登录qq邮箱发邮件的测试'

# ssl登录
smtp = SMTP_SSL(host_server)
smtp.ehlo(host_server)
smtp.login(sender_qq, pwd)

sender_qq_mail = sender_qq + '@qq.com'  # 发件人的邮箱
msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = receiver
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
