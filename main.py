# -*- encoding: UTF-8 -*-
'''
@File    :  main.py
@Time    :  2021/02/27 23:18:17
@Author  :  Kearney
@Contact :  191615342@qq.com
@Desc    :  定时触发脚本
'''
import schedule
import time
import datetime
import os
from mail import sendMail


def job():
    content = str(datetime.datetime.now()) + 'Loving you'
    sendMail(qq=os.getenv('QQ'),
             pwd=os.getenv('PWD'),
             receiver=os.getenv('MAIL_RECEIVER'),
             mail_content=content)


schedule.every(30).seconds.do(job)
# schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
