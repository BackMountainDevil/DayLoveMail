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


def sendMail(qq,
             pwd,
             receiver,
             title='Loving you.',
             mail_content="Love forever"):
    """用QQ邮箱发送邮件
    参数：
        qq              发信人QQ，如“191716520”
        pwd             发信人QQ邮箱SMTP授权码，非邮箱密码
        receiver        收信人邮箱，如“191715520@163.com”
        title           邮件标题
        mail_content    邮件正文（内容）
    返回值：
        发送成功返回True
        其它异常则返回异常信息
    """
    host_server = 'smtp.qq.com'  # qq邮箱smtp服务器
    sender_qq_mail = qq + '@qq.com'  # 发件人的邮箱
    try:
        smtp = SMTP_SSL(host_server)
        smtp.ehlo(host_server)
        smtp.login(qq, pwd)
        msg = MIMEText(mail_content, "plain", 'utf-8')
        msg["Subject"] = Header(title, 'utf-8')
        msg["From"] = sender_qq_mail
        msg["To"] = receiver
        smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
        smtp.quit()
        return True
    except Exception as e:
        return e
