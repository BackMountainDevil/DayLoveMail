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
import os
import requests
from mail import sendMail


def job():
    r = requests.get('http://open.iciba.com/dsapi/').json()
    sendMail(qq=os.getenv('QQ'),
             pwd=os.getenv('PWD'),
             receiver=os.getenv('MAIL_RECEIVER'),
             mail_content=r['note'])


schedule.every().day.at("5:20").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
